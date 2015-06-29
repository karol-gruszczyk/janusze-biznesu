from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .updater import Updater


@login_required
def updater_status(request):
    Updater()
    return render(request, 'updater/status.html', {})


@login_required
def updater_status_api(request):
    data = Updater().get_update_status()
    return JsonResponse(data)


@login_required
def import_whole_view(request):
    Updater().import_whole_database()
    return render(request, 'updater/update.html', {})


@login_required
def import_few_last_view(request):
    Updater().import_few_last()
    return render(request, 'updater/update.html', {})
