from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin
from .models import Share, ShareGroup


class ShareListView(LoginRequiredMixin, ListView):
    model = Share
    template_name = 'shares/share_list.html'


class GroupListView(LoginRequiredMixin, ListView):
    model = ShareGroup
    template_name = 'shares/groups/group_list.html'


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = ShareGroup
    fields = ['name', 'shares']
    template_name = 'shares/groups/group_create.html'
    success_url = reverse_lazy('shares:group-list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = ShareGroup
    template_name = 'shares/groups/group_delete.html'
    success_url = reverse_lazy('shares:group-list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = ShareGroup
    template_name = 'shares/groups/group_update.html'
    fields = ['name', 'shares']
    success_url = reverse_lazy('shares:group-list')
