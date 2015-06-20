from django.shortcuts import render
from django.http import JsonResponse
from .handlers import SystemMonitor


def general_info(request):
    data = SystemMonitor().get_general_info()
    return render(request, 'stats/general.html', data)


def cpu_info(request):
    return render(request, 'stats/cpu.html')


def memory_info(request):
    return render(request, 'stats/memory.html')


def network_info(request):
    return render(request, 'stats/network.html')
