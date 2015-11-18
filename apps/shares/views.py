from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from utils.views import SortableListView
from .models import Share, ShareGroup
from .forms import ShareGroupForm


class ShareListView(LoginRequiredMixin, SortableListView):
    model = Share
    template_name = 'shares/share_list.html'
    sort_by = ['name', 'records', 'first_record', 'last_record']
    default_sort_by = '-last_record'


class ShareUpdateView(LoginRequiredMixin, UpdateView):
    model = Share
    template_name = 'shares/share_update.html'
    fields = ['verbose_name', 'updated_daily']
    success_url = reverse_lazy('shares:share-list')


class ShareDetailView(LoginRequiredMixin, DetailView):
    model = Share
    template_name = 'shares/share_detail.html'


class GroupListView(LoginRequiredMixin, ListView):
    model = ShareGroup
    template_name = 'shares/groups/group_list.html'


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = ShareGroup
    form_class = ShareGroupForm
    template_name = 'shares/groups/group_form.html'
    success_url = reverse_lazy('shares:group-list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = ShareGroup
    template_name = 'shares/groups/group_delete.html'
    success_url = reverse_lazy('shares:group-list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = ShareGroup
    form_class = ShareGroupForm
    template_name = 'shares/groups/group_update.html'
    success_url = reverse_lazy('shares:group-list')


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = ShareGroup
    template_name = 'shares/groups/group_form.html'
