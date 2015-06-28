from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
from .models import Share, ShareRecord, ShareGroup


class ShareListView(LoginRequiredMixin, ListView):
    model = Share
    template_name = 'shares/share_list.html'
    queryset = Share.objects.all().order_by('-last_record', '-records')


class ShareUpdateView(LoginRequiredMixin, UpdateView):
    model = Share
    template_name = 'shares/share_update.html'
    fields = ['visible_name', 'updated_daily']
    success_url = reverse_lazy('shares:share-list')


class ShareRecordListView(LoginRequiredMixin, ListView):
    model = ShareRecord
    template_name = 'shares/share_record_list.html'

    def get_queryset(self):
        qs = super(ShareRecordListView, self).get_queryset()
        return qs.filter(share__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ShareRecordListView, self).get_context_data()
        context['share'] = get_object_or_404(Share, pk=self.kwargs['pk'])
        return context


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
