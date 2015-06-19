from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin
from .models import Share


class ShareListView(LoginRequiredMixin, ListView):

    model = Share
    template_name = 'shares/share_list.html'
