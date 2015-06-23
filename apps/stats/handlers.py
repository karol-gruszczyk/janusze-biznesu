import psutil
import socket
import platform
import subprocess
import uuid
import re
from threading import Timer
from datetime import datetime


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("robie")
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
    cpu_load_stats = []
    network_traffic_stats = []

    def __init__(self):
        self.hostname = platform.node()
        self.architecture = platform.architecture()[0]
        self.python_version = platform.python_version()
        self.os = platform.system() + ' ' + platform.uname().release
        self.ram_total = psutil.virtual_memory().total
        self.swap_total = psutil.swap_memory().total
        time = datetime.fromtimestamp(psutil.boot_time())
        self.boot_time = datetime(time.year, time.month, time.day, time.hour, time.minute)
        self._init_cpu()
        self.network_traffic_stats = [['time', 'download', 'upload']]
        self.net_bytes_sent = psutil.net_io_counters().bytes_sent
        self.net_bytes_received = psutil.net_io_counters().bytes_recv
        self.stats_timer_interval = 10
        self.stats_timer = None
        self.global_data = {'stats_interval': self.stats_timer_interval * 1000}
        self.update_stats()

    def __del__(self):
        if self.stats_timer:
            self.stats_timer.stop()

    def update_stats(self):
        time_now = str(datetime.now().time()).split('.')[0]
        self.cpu_load_stats.append([time_now] + psutil.cpu_percent(percpu=True))
        if len(self.cpu_load_stats) > 61:
            del self.cpu_load_stats[1]
        net_io = psutil.net_io_counters()
        div = (2 << 16) * self.stats_timer_interval
        d_sent = (net_io.bytes_sent - self.net_bytes_sent) / div
        d_received = (net_io.bytes_recv - self.net_bytes_received) / div
        self.net_bytes_sent = net_io.bytes_sent
        self.net_bytes_received = net_io.bytes_recv
        self.network_traffic_stats.append([time_now, d_received, d_sent])
        if len(self.network_traffic_stats) > 61:
            del self.network_traffic_stats[1]
        self.stats_timer = Timer(self.stats_timer_interval, self.update_stats).start()

    def _init_cpu(self):
        if platform.system().lower() == 'windows':
            self.cpu_name = platform.processor()
        elif platform.system().lower() == 'linux':
            all_info = str(subprocess.check_output('cat /proc/cpuinfo', shell=True).strip())
            for line in all_info.split('\\n'):
                if 'model name' in line:
                    self.cpu_name = re.sub(r'.*model name.*:', '', line, 1)
        self.cpu_count = psutil.cpu_count(logical=False)
        self.cpu_logical_count = psutil.cpu_count()
        self.cpu_load_stats = [['time'] + ['Core #' + str(i) for i in range(self.cpu_logical_count)]]

    def get_general_info(self):
        disk_total = sum([psutil.disk_usage(dev.mountpoint).total for dev in psutil.disk_partitions()])
        data = {
            'os': self.os,
            'architecture': self.architecture,
            'hostname': self.hostname,
            'cpu': self.cpu_name,
            'python_version': self.python_version,
            'boot_time': self.boot_time,
            'up_time': str(datetime.now() - self.boot_time).split('.')[0],  # removing microseconds
            'total_ram_mem': format_bytes(self.ram_total),
            'total_swap_mem': format_bytes(self.swap_total),
            'total_disk_mem': format_bytes(disk_total)
        }
        return data

    def get_cpu_info(self):
        data = {
            'name': self.cpu_name,
            'count': self.cpu_count,
            'logical_count': self.cpu_logical_count,
            'load': psutil.cpu_percent(),
            'temperature': 'over 9000',
        }
        data.update(self.global_data)
        return data

    def get_network_info(self):
        data = {
            'hostname': self.hostname,
            'mac_address': ':'.join(("%012X" % uuid.getnode())[i:i + 2] for i in range(0, 12, 2)),
            'ip_address': socket.gethostbyname(socket.gethostname()),
            'bytes_sent': format_bytes(self.net_bytes_sent),
            'bytes_received': format_bytes(self.net_bytes_received)
        }
        data.update(self.global_data)
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
