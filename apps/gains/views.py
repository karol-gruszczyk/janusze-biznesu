from django.db.models import Max

from braces.views import LoginRequiredMixin

from utils.views import SortableListView
from .models import Gain


class GainListView(SortableListView, LoginRequiredMixin):
    model = Gain
    sort_by = ['close_gain', 'open_gain', 'high_gain', 'low_gain', 'volume_gain']
    default_sort_by = '-close_gain'

    def get_queryset(self):
        max_date = Gain.objects.all().aggregate(Max('date'))['date__max']
        return super(GainListView, self).get_queryset().filter(date=max_date)[:20]
