from django.conf.urls import url, patterns

from .api_views import ShareListAPIView, ShareRecordListAPIView

urlpatterns = patterns(
    '',
    url(r'^$', ShareListAPIView.as_view(), name='share-list'),
    url(r'^records/(?P<pk>[\w-]+)$', ShareRecordListAPIView.as_view(), name='record-list'),
)
