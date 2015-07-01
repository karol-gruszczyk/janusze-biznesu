from django.conf.urls import patterns, url
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskDetailView, TaskUpdateView

urlpatterns = patterns(
    '',
    url(r'^list/$', TaskListView.as_view(), name='task-list'),
    url(r'^create/$', TaskCreateView.as_view(), name='task-create'),
    url(r'^detail/(?P<pk>[\w-]+)$', TaskDetailView.as_view(), name='task-detail'),
    url(r'^update/(?P<pk>[\w-]+)$', TaskUpdateView.as_view(), name='task-update'),
    url(r'^delete/(?P<pk>[\w-]+)$', TaskDeleteView.as_view(), name='task-delete'),
)
