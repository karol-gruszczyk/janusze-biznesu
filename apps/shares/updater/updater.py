import wget
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from collections import namedtuple
from threading import Thread
from utils import Singleton

DownloadStatus = namedtuple('DownloadStatus', 'done total percent')


class Updater(metaclass=Singleton):
    update_status = {}
    is_updating = False
    thread = None

    def __init__(self):
        self.update_status = {
            'current_file': {
                'done': filesizeformat(0),
                'total': filesizeformat(0),
                'percent': 0,
                'name': 'none'
            },
            'download_progress': {
                'current': 0,
                'total': 0,
                'percent': 0
            },
            'processing_progress': {
                'current': 0,
                'total': 0,
                'percent': 50
            }
        }

    def get_update_status(self):
        return self.update_status

    def download_func(self, current, total, width=None):
        self.update_status['current_file']['done'] = filesizeformat(current)
        self.update_status['current_file']['total'] = filesizeformat(total)
        self.update_status['current_file']['percent'] = round(current / total * 100)
        return ''

    def update_whole_database(self):
        if not self.thread:
            self.thread = Thread(target=self.update_whole_database)
            self.thread.start()
            return
        if not self.is_updating:
            self.is_updating = True
            self.update_status['download_progress']['current'] = 0
            self.update_status['download_progress']['total'] = len(settings.DATABASE_SOURCE_URLS)
            self.update_status['download_progress']['percent'] = 0
            for key, value in settings.DATABASE_SOURCE_URLS.items():
                self.update_status['current_file']['name'] = value
                filepath = wget.download(url=value, out="/tmp", bar=self.download_func)
                self.update_status['download_progress']['current'] += 1
                self.update_status['download_progress']['percent'] = round(
                    self.update_status['download_progress']['current']
                    / self.update_status['download_progress']['total'] * 100)

            self.is_updating = False
            self.thread = None
        else:
            return
