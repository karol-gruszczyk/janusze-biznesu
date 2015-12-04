from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, DeleteView
from braces.views import LoginRequiredMixin

from .models import TaskStatus


class TaskTaskStatusListView(LoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = 'tasks/task_list.html'


class TaskStatusDetailView(LoginRequiredMixin, DetailView):
    model = TaskStatus
    template_name = 'tasks/task_detail.html'


class TaskStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskStatus
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')
