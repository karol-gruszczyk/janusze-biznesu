from django.conf.urls import url, patterns

from .views import updater_status, updater_status_api, import_whole_view, import_few_last_view

urlpatterns = patterns(
    '',
    url(r'^$', updater_status, name='status'),
    url(r'^import-db/$', import_whole_view, name='import-db'),
    url(r'^import-few-last/$', import_few_last_view, name='import-few-last'),
    url(r'^api/$', updater_status_api, name='status-api'),
)
