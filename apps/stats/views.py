from django.shortcuts import render
from .handlers import SystemMonitor


def general_info(request):
    data = SystemMonitor().get_general_info()
    return render(request, 'stats/general.html', data)


def cpu_info(request):
    data = SystemMonitor().get_cpu_info()
    return render(request, 'stats/cpu.html', {'cpu': data})


def memory_info(request):
    disks = SystemMonitor().get_disk_info()
    ram = SystemMonitor().get_ram_info()
    swap = SystemMonitor().get_swap_info()
    return render(request, 'stats/memory.html', {'disks': disks, 'ram': ram, 'swap': swap})


def network_info(request):
    data = SystemMonitor().get_network_info()
    return render(request, 'stats/network.html', data)
