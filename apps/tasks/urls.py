from django.conf.urls import patterns, url
from .views import TaskTaskStatusListView, TaskStatusDeleteView


urlpatterns = patterns(
    '',
    url(r'^list/$', TaskTaskStatusListView.as_view(), name='task-list'),
    # url(r'^create-correlation-task/$', CorrelationTaskCreateView.as_view(), name='correlation-task-create'),
    url(r'^delete/(?P<pk>[\w-]+)$', TaskStatusDeleteView.as_view(), name='task-delete'),
)
