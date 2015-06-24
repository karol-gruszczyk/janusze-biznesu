from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .monitor import SystemMonitor


@login_required
def general_info(request):
    data = SystemMonitor().get_general_info()
    return render(request, 'stats/general.html', data)


@login_required
def cpu_info(request):
    data = SystemMonitor().get_cpu_info()
    return render(request, 'stats/cpu.html', data)


@login_required
def cpu_load(request):
    return JsonResponse({'load_stats': SystemMonitor().cpu_load_stats, 'temp_stats': SystemMonitor().cpu_temp_stats})


@login_required
def network_traffic(request):
    return JsonResponse({'traffic_stats': SystemMonitor().network_traffic_stats})


@login_required
def memory_info(request):
    disks = SystemMonitor().get_disk_info()
    ram = SystemMonitor().get_ram_info()
    swap = SystemMonitor().get_swap_info()
    return render(request, 'stats/memory.html', {'disks': disks, 'ram': ram, 'swap': swap})


@login_required
def network_info(request):
    data = SystemMonitor().get_network_info()
    return render(request, 'stats/network.html', data)
