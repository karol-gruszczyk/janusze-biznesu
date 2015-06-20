from django.conf.urls import url, patterns

from .views import ShareListView, GroupCreateView, GroupListView, GroupDeleteView, GroupUpdateView

urlpatterns = patterns(
    '',
    url(r'^$', ShareListView.as_view(), name='share-list'),
    url(r'groups/list$', GroupListView.as_view(), name='group-list'),
    url(r'groups/create$', GroupCreateView.as_view(), name='group-create'),
    url(r'groups/update/(?P<pk>[\w-]+)$', GroupUpdateView.as_view(), name='group-update'),
    url(r'groups/delete/(?P<pk>[\w-]+)$', GroupDeleteView.as_view(), name='group-delete'),
)