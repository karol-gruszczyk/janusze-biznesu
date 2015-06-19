from django.conf.urls import url, patterns

from .views import ShareListView

urlpatterns = patterns(
    '',
    url(r'^$', ShareListView.as_view(), name='share-list'),
)