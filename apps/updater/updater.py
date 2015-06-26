import os
import shutil
from threading import Thread
from datetime import datetime
from zipfile import ZipFile
from django.conf import settings
from django.template.defaultfilters import filesizeformat
import wget
from utils import Singleton
from apps.shares.models import Share, ShareRecord


class Updater(metaclass=Singleton):
    update_status = {}
    is_updating = False
    thread = None

    def __init__(self):
        self.init_status()

    def get_update_status(self):
        return self.update_status

    def init_status(self):
        self.update_status = {
            'file': {
                'done': filesizeformat(0),
                'total': filesizeformat(0),
                'percent': 0,
                'name': 'none'
            },
            'download': {
                'current': 0,
                'total': len(settings.DATABASE_SOURCE_URLS),
                'percent': 0
            },
            'processing': {
                'action': 'waiting for download to complete',
                'current': 0,
                'total': len(settings.DATABASE_SOURCE_URLS),
                'percent': 0
            }
        }

    def download_files(self):
        def __download_func(current, total, width=None):
            self.update_status['file']['done'] = filesizeformat(current)
            self.update_status['file']['total'] = filesizeformat(total)
            self.update_status['file']['percent'] = round(current / total * 100)
            return ''

        dl_files = {}
        for key, value in settings.DATABASE_SOURCE_URLS.items():
            self.update_status['file']['name'] = value
            file_path = wget.download(url=value, out='/tmp', bar=__download_func)
            dl_files[key] = file_path
            self.update_status['download']['current'] += 1
            self.update_status['download']['percent'] = round(self.update_status['download']['current']
                                                              / self.update_status['download']['total'] * 100)
        return dl_files

    def extract_zip_files(self, files):
        self.update_status['processing']['action'] = 'extracting files'
        path_dirs = {}
        for db_type, path in files.items():
            dir_name = path + '_unpack'
            path_dirs[db_type] = dir_name
            with ZipFile(path, 'r') as zf:
                zf.extractall(path=dir_name)
            self.update_status['processing']['current'] += 1
        return path_dirs

    @classmethod
    def get_record_from_line(cls, share, line):
        cols = line.strip().split(',')  # assuming format is: Name,Date,Open,High,Low,Close,Volume
        date = datetime.strptime(cols[1], '%Y%M%d')
        return ShareRecord(share=share, date=date, open=cols[2], high=cols[3],
                           low=cols[4], close=cols[5], volume=cols[6])

    @classmethod
    def update_share(cls, file_name, db_type):
        share_name = os.path.splitext(file_name)[0]
        share = Share.objects.update_or_create(name=share_name)[0]
        return share

    def process_files(self, dirs):
        self.update_status['processing']['action'] = 'parsing files'
        self.update_status['processing']['current'] = 0
        self.update_status['processing']['total'] = sum(len(os.listdir(i)) for i in dirs.values())
        ShareRecord.objects.all().delete()
        for db_type, path_name in dirs.items():
            for file_name in os.listdir(path_name):
                with open(os.path.join(path_name, file_name), 'r') as f:
                    f.readline()
                    share = self.update_share(file_name, db_type)
                    ShareRecord.objects.bulk_create([self.get_record_from_line(share, line) for line in f.readlines()])
                self.update_status['processing']['current'] += 1
                self.update_status['processing']['percent'] = round(self.update_status['processing']['current']
                                                                    / self.update_status['processing']['total'] * 100)

    def clean_up(self, dl_files, dl_dirs):
        self.update_status['processing']['action'] = 'cleaning up'
        for dl_file in dl_files.values():
            os.remove(dl_file)
        for dl_dir in dl_dirs.values():
            shutil.rmtree(dl_dir)
        self.update_status['processing']['action'] = 'done'

    def update_whole_database(self):
        if not self.thread:
            self.thread = Thread(target=self.update_whole_database)
            self.thread.start()
            return
        if not self.is_updating:
            self.is_updating = True
            self.init_status()
            dl_files = self.download_files()
            dl_dirs = self.extract_zip_files(dl_files)
            self.process_files(dl_dirs)
            self.clean_up(dl_files, dl_dirs)
            self.is_updating = False
            self.thread = None
        else:
            return
