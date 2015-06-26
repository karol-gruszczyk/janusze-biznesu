from django.conf.urls import url, patterns

from .views import updater_status, updater_status_api, full_import

urlpatterns = patterns(
    '',
    url(r'^$', updater_status, name='status'),
    url(r'^full-import/$', full_import, name='full-import'),
    url(r'^api/$', updater_status_api, name='status-api'),
)
