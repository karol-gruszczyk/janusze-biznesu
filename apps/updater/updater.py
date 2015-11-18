import os
import shutil
from threading import Thread
from datetime import datetime
from zipfile import ZipFile

from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.db.models import Max

import pytz
import wget
import requests
from utils import Singleton

from apps.shares.models import Share, ShareRecord, ShareGroup
from apps.gains.models import Gain


class Updater(metaclass=Singleton):
    update_status = {}
    is_updating = False
    thread = None

    def __init__(self):
        self.init_statuses()

    def get_update_status(self):
        return self.update_status

    def init_statuses(self):
        self.update_status = {
            'file': {},
            'download': {},
            'processing': {}
        }
        self.init_status(self.update_status['file'], 'Waiting ...', 0)
        self.init_status(self.update_status['download'], 'Waiting ...', 0)
        self.init_status(self.update_status['processing'], 'Waiting ...', 0)

    @classmethod
    def init_status(cls, status, job, total):
        status['current'] = 0
        status['percent'] = 0
        status['total'] = total
        status['job'] = job

    @classmethod
    def update_percent(cls, status):
        status['percent'] = round(status['current'] / status['total'] * 100)

    @classmethod
    def increment_status(cls, status):
        status['current'] += 1
        cls.update_percent(status)

    def download_file(self, file_url):
        def __download_func(current, total, width=None):
            self.update_status['file']['current'] = current
            self.update_status['file']['total'] = total
            self.update_percent(self.update_status['file'])
            self.update_status['file']['current'] = filesizeformat(current)
            self.update_status['file']['total'] = filesizeformat(total)
            return ''

        self.update_status['file']['job'] = 'Downloading {} ...'.format(file_url)
        file_path = wget.download(url=file_url, out='/tmp', bar=__download_func)
        self.increment_status(self.update_status['download'])
        return file_path

    def download_files(self, files):
        self.init_status(self.update_status['download'], 'Downloading ...', len(files))
        dl_files = {}
        for key, value in files.items():
            dl_files[key] = self.download_file(value)
        self.update_status['file']['job'] = 'Done.'
        self.update_status['download']['job'] = 'Done.'
        return dl_files

    def extract_zip_files(self, files):
        self.update_status['processing']['job'] = 'Extracting files ...'  # fast, no need for percent
        path_dirs = {}
        for db_type, path in files.items():
            dir_name = path + '_unpack'
            path_dirs[db_type] = dir_name
            with ZipFile(path, 'r') as zf:
                zf.extractall(path=dir_name)
        return path_dirs

    @classmethod
    def get_record_from_line(cls, share, line):
        cols = line.strip().split(',')  # assuming format is: Name,Date,Open,High,Low,Close,Volume
        date = datetime.strptime(cols[1], '%Y%m%d')
        return ShareRecord(share=share, date=date, open=cols[2], high=cols[3],
                           low=cols[4], close=cols[5], volume=cols[6])

    @classmethod
    def create_record_from_line(cls, line):
        cols = line.strip().split(',')  # assuming format is: Name,Date,Open,High,Low,Close,Volume
        name = cols[0]
        date = datetime.strptime(cols[1], '%Y%m%d')
        if not ShareRecord.objects.filter(share__name=name, date=date).exists():
            share, created = Share.objects.get_or_create(name=name)
            max_date = ShareRecord.objects.filter(share=share).aggregate(Max('date'))['date__max']
            lower_record = ShareRecord.objects.get(share=share, date=max_date)
            upper_record = ShareRecord.objects.create(share=share, date=date, open=float(cols[2]), high=float(cols[3]),
                                                      low=float(cols[4]), close=float(cols[5]), volume=float(cols[6]))
            per_gain = lambda first, second: (second - first) / first if first else 0  # returning percentage gain
            Gain.objects.create(share=share, date=upper_record.date,
                                lower_record=lower_record, upper_record=upper_record,
                                volume_gain=per_gain(lower_record.volume, upper_record.volume),
                                open_gain=per_gain(lower_record.open, upper_record.open),
                                close_gain=per_gain(lower_record.close, upper_record.close),
                                high_gain=per_gain(lower_record.high, upper_record.high),
                                low_gain=per_gain(lower_record.low, upper_record.low))

    def import_share(self, path_name, file_name, group_name):
        with open(os.path.join(path_name, file_name), 'r') as f:
            f.readline()
            share_name = os.path.splitext(file_name)[0]
            share, created = Share.objects.get_or_create(name=share_name)
            records = [self.get_record_from_line(share, line) for line in f.readlines()]
        share.first_record = records[0].date
        share.last_record = records[-1].date
        share.records = len(records)
        share.save()
        ShareRecord.objects.bulk_create(records)
        gains = []
        per_gain = lambda first, second: (second - first) / first if first else 0  # returning percentage gain
        records = ShareRecord.objects.filter(share=share)
        for lower_record, upper_record in zip(records[:len(records) - 1], records[1:]):
            gain = Gain(share=share, date=upper_record.date,
                        lower_record=lower_record, upper_record=upper_record,
                        volume_gain=per_gain(lower_record.volume, upper_record.volume),
                        open_gain=per_gain(lower_record.open, upper_record.open),
                        close_gain=per_gain(lower_record.close, upper_record.close),
                        high_gain=per_gain(lower_record.high, upper_record.high),
                        low_gain=per_gain(lower_record.low, upper_record.low))
            gains.append(gain)
        Gain.objects.bulk_create(gains)
        group = ShareGroup.objects.update_or_create(name=group_name)[0]
        group.shares.add(share)
        self.increment_status(self.update_status['processing'])

    def process_db_files(self, dirs):
        total = sum(len(os.listdir(i)) for i in dirs.values())
        self.init_status(self.update_status['processing'], 'Parsing files ...', total)
        ShareRecord.objects.all().delete()
        Gain.objects.all().delete()
        for group, path_name in dirs.items():
            for file_name in os.listdir(path_name):
                self.import_share(path_name, file_name, group)
        self.get_additional_info()

    def process_day_files(self, path):
        file_names = os.listdir(path)
        self.init_status(self.update_status['processing'], 'Parsing files ...', len(file_names))
        for file_name in file_names:
            with open(os.path.join(path, file_name), 'r') as f:
                for line in f.readlines():
                    self.create_record_from_line(line)
            self.increment_status(self.update_status['processing'])
        self.get_additional_info()

    def get_additional_info(self):
        lines = requests.get(settings.DATABASE_LIST_URL).text.split('\n')[3:-3]
        self.init_status(self.update_status['processing'], 'Updating database info ...', len(lines))
        for line in lines:  # 3 first and 2 last lines contain file info
            info = line.strip().split()
            name = info[4].strip('.txt')
            self.increment_status(self.update_status['processing'])
            try:
                share = Share.objects.get(name=name)
            except Share.DoesNotExist:
                continue
            date = datetime.strptime(" ".join(info[0:2]), "%Y-%m-%d %H:%M")
            date.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
            verbose_name = " ".join(info[5:])
            share.last_updated = date
            share.verbose_name = verbose_name
            share.save()

    def clean_up(self, dl_files, dl_dirs):
        self.update_status['processing']['job'] = 'Cleaning up ...'
        for dl_file in dl_files.values():
            os.remove(dl_file)
        for dl_dir in dl_dirs.values():
            shutil.rmtree(dl_dir)
        self.update_status['processing']['job'] = 'Done.'

    def import_whole_database(self):
        if not self.thread:
            self.thread = Thread(target=self.import_whole_database)
            self.thread.start()
        elif not self.is_updating:
            self.is_updating = True
            self.init_statuses()
            dl_files = self.download_files(settings.DATABASE_SOURCE_URLS)
            dl_dirs = self.extract_zip_files(dl_files)
            self.process_db_files(dl_dirs)
            self.get_additional_info()
            self.clean_up(dl_files, dl_dirs)
            self.is_updating = False
            self.thread = None

    def import_few_last(self):
        if not self.thread:
            self.thread = Thread(target=self.import_few_last)
            self.thread.start()
        elif not self.is_updating:
            self.is_updating = True
            self.init_statuses()
            self.update_status['download']['total'] = 1
            dl_file = self.download_files({'few_last': settings.DATABASE_UPDATE_URL})
            dl_dir = self.extract_zip_files(dl_file)
            self.process_day_files(dl_dir['few_last'])
            self.clean_up(dl_file, dl_dir)
            self.is_updating = False
            self.thread = None
