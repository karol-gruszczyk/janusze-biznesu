from pyspectator.computer import Computer
from datetime import datetime


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def format_bytes(number):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    suffix = 0
    while True:
        if number < 1024:
            return str(round(number, 2)) + " " + suffixes[suffix]
        number /= 1024
        suffix += 1


class SystemMonitor(metaclass=Singleton):

    def __init__(self):
        self.computer_info = Computer()

    @property
    def cpu_info(self):
        return self.computer_info.processor

    @property
    def memory_info(self):
        return self.computer_info.virtual_memory

    @property
    def disk_info(self):
        return self.computer_info.nonvolatile_memory

    def get_general_info(self):
        data = {
            'os': self.computer_info.os,
            'architecture': self.computer_info.architecture,
            'hostname': self.computer_info.hostname,
            'cpu': self.cpu_info.name,
            'python_version': self.computer_info.python_version,
            'boot_time': datetime.now() - self.computer_info.raw_uptime,
            'up_time': self.computer_info.uptime,
            'total_ram_mem': format_bytes(self.memory_info.total),
            'total_disk_mem': format_bytes(sum([dev.total for dev in self.disk_info]))
        }
        return data
