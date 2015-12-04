from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin

from utils.views import SortableListView
from .models import Correlation, CorrelationSet
from .forms import CorrelationSetForm


class CorrelationListView(LoginRequiredMixin, SortableListView):
    model = Correlation
    sort_by = ['value', 'day_interval']
    default_sort_by = 'value'


class CorrelationSetCreateView(LoginRequiredMixin, CreateView):
    model = CorrelationSet
    form_class = CorrelationSetForm
    success_url = reverse_lazy('correlations:correlation-set-list')


class CorrelationSetListView(LoginRequiredMixin, ListView):
    model = CorrelationSet
    fields = ['name', 'shares']
    template_name = 'correlations/correlationset_list.html'


class CorrelationSetUpdateView(LoginRequiredMixin, UpdateView):
    model = CorrelationSet
    form_class = CorrelationSetForm
    success_url = reverse_lazy('correlations:correlation-set-list')


class CorrelationSetDeleteView(LoginRequiredMixin, DeleteView):
    model = CorrelationSet
    success_url = reverse_lazy('correlations:correlation-set-list')
