from django.conf.urls import url, patterns

from .views import general_info, cpu_info, memory_info, network_info, cpu_load, network_traffic

urlpatterns = patterns(
    '',
    url(r'^$', general_info, name='general'),
    url(r'^cpu/$', cpu_info, name='cpu'),
    url(r'^memory/$', memory_info, name='memory'),
    url(r'^network/$', network_info, name='network'),
    url(r'^cpu/api/$', cpu_load, name='api-cpu'),
    url(r'^network/api/$', network_traffic, name='api-network'),
)