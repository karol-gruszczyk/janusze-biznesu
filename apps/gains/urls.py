from django.conf.urls import patterns, url
from .views import GainListView


urlpatterns = patterns(
    '',
    url(r'^$', GainListView.as_view(), name='gain-list'),
)
