from django.views.generic import ListView
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect


class SortableListView(ListView):
    sort_by = None
    default_sort_by = None

    def __init__(self, **kwargs):
        super(SortableListView, self).__init__(**kwargs)
        if not self.sort_by:
            raise ImproperlyConfigured('sort_by in {} is empty'.format(self.__class__.__name__))
        if not self.default_sort_by:
            raise ImproperlyConfigured('default_sort_by in {} is empty'.format(self.__class__.__name__))

    def get_queryset(self):
        return super(SortableListView, self).get_queryset().order_by(self.get_sort_by())

    def get(self, request, *args, **kwargs):
        sort_by = self.request.GET.get('sort_by')
        if not sort_by or sort_by not in self.sort_by and (sort_by[1:] not in self.sort_by or sort_by[0] != '-'):
            return HttpResponseRedirect(request.path + '?sort_by={}'.format(self.default_sort_by))
        return super(SortableListView, self).get(request, *args, **kwargs)

    def get_sort_by(self):
        return self.request.GET.get('sort_by', self.default_sort_by)
