from django.conf.urls import patterns, url

from .views import CorrelationListView, CorrelationSetCreateView, CorrelationSetListView, \
    CorrelationSetUpdateView, CorrelationSetDeleteView


urlpatterns = patterns(
    '',
    url('^correlation-list/$', CorrelationListView.as_view(), name='correlation-list'),
    url('^correlation-set-create/$', CorrelationSetCreateView.as_view(), name='correlation-set-create'),
    url('^correlation-set-list/$', CorrelationSetListView.as_view(), name='correlation-set-list'),
    url('^correlation-set-update/(?P<pk>[\w-]+)$', CorrelationSetUpdateView.as_view(), name='correlation-set-update'),
    url('^correlation-set-delete/(?P<pk>[\w-]+)$', CorrelationSetDeleteView.as_view(), name='correlation-set-delete'),
)
