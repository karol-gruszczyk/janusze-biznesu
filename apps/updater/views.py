from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .updater import Updater
from apps.shares.models import Share


@login_required
def updater_status(request):
    last_update = Share.objects.all().latest().last_updated
    data = {
        'is_updating': Updater().is_updating,
        'last_update': last_update
    }
    return render(request, 'updater/status.html', data)


@login_required
def updater_status_api(request):
    data = Updater().get_update_status()
    return JsonResponse(data)


@login_required
def import_whole_view(request):
    Updater().import_whole_database()
    return redirect('updater:status')


@login_required
def import_few_last_view(request):
    Updater().import_few_last()
    return redirect('updater:status')
