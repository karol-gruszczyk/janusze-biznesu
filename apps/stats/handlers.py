import psutil
import platform
from _datetime import datetime


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
        if number < 1024 or suffix >= 4:
            return str(round(number, 2)) + " " + suffixes[suffix]
        number /= 1024
        suffix += 1


class SystemMonitor(metaclass=Singleton):

    def __init__(self):
        self.hostname = platform.node()
        self.architecture = platform.architecture()[0]
        self.cpu_name = platform.processor()
        self.python_version = platform.python_version()
        self.os = platform.system() + ' ' + platform.uname().release
        self.ram_total = psutil.virtual_memory().total
        self.swap_total = psutil.swap_memory().total
        self.boot_time = datetime.fromtimestamp(psutil.boot_time())
        self._init_cpu()

    def _init_cpu(self):
        self.cpu_count = psutil.cpu_count(logical=False)
        self.cpu_logical_count = psutil.cpu_count()

    def get_general_info(self):
        data = {
            'os': self.os,
            'architecture': self.architecture,
            'hostname': self.hostname,
            'cpu': self.cpu_name,
            'python_version': self.python_version,
            'boot_time': self.boot_time,
            # 'up_time': self.computer_info.uptime,
            'total_ram_mem': format_bytes(self.ram_total),
            'total_swap_mem': format_bytes(self.swap_total),
            # 'total_disk_mem': format_bytes(sum([dev.total for dev in self.disk_info]))
        }
        return data

    def get_cpu_info(self):
        data = {
            # 'name': self.cpu_info.name,
            'count': self.cpu_count,
            'logical_count': self.cpu_logical_count,
            'load': psutil.cpu_percent(),
            # 'temperature': len(self.cpu_info.load_stats),
            # 'load_stats': self.cpu_info.load_stats
        }
        return data

    def get_network_info(self):
        netio = psutil.net_io_counters()
        data = {
            'hostname': self.hostname,
            # 'mac_address': self.network_info.hardware_address,
            # 'ip_address': self.network_info.ip_address,
            # 'mask': self.network_info.subnet_mask,
            # 'gateway': self.network_info.default_route,
            'bytes_sent': format_bytes(netio.bytes_sent),
            'bytes_received': format_bytes(netio.bytes_recv)
        }
        return data

    @classmethod
    def get_ram_info(cls):
        ram = psutil.virtual_memory()
        data = {
            'used': format_bytes(ram.total * ram.percent / 100),
            'total': format_bytes(ram.total),
            'used_percent': ram.percent,
        }
        return data

    @classmethod
    def get_swap_info(cls):
        swap = psutil.swap_memory()
        data = {
            'used': format_bytes(swap.total * swap.percent / 100),
            'total': format_bytes(swap.total),
            'used_percent': swap.percent,
        }
        return data

    @classmethod
    def get_disk_info(cls):
        data = []
        for dev in psutil.disk_partitions():
            usage = psutil.disk_usage(dev.mountpoint)
            data.append({
                'device': dev.device,
                'mount_point': dev.mountpoint,
                'fs_type': dev.fstype,
                'used': format_bytes(usage.used),
                'total': format_bytes(usage.total),
                'used_percent': usage.percent
            })
        return data
