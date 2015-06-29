from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin
from .models import Share, ShareGroup


class ShareListView(LoginRequiredMixin, ListView):
    model = Share
    template_name = 'shares/share_list.html'
    queryset = Share.objects.all().order_by('-last_record', '-records')


class ShareUpdateView(LoginRequiredMixin, UpdateView):
    model = Share
    template_name = 'shares/share_update.html'
    fields = ['visible_name', 'updated_daily']
    success_url = reverse_lazy('shares:share-list')


class ShareDetailView(LoginRequiredMixin, DetailView):
    model = Share
    template_name = 'shares/share_detail.html'


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
    fields = ['visible_name', 'shares']
    success_url = reverse_lazy('shares:group-list')
