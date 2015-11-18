from django.views.generic import ListView
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect


class SortableListView(ListView):
    sort_by = None
    default_sort_by = None

    def __init__(self, **kwargs):
        super(SortableListView, self).__init__(**kwargs)
        if not self.sort_by:
            raise ImproperlyConfigured('sort_by in {} is empty'.format(self.__name__))
        if not self.default_sort_by:
            raise ImproperlyConfigured('default_sort_by in {} is empty'.format(self.__name__))

    def get_queryset(self):
        return super(SortableListView, self).get_queryset().order_by(self.get_sort_by())

    def get(self, request, *args, **kwargs):
        if 'sort_by' not in request.GET:
            response = redirect('gains:gain-list')
            response['Location'] += '?sort_by={}'.format(self.default_sort_by)
            return response
        return super(SortableListView, self).get(request, *args, **kwargs)

    def get_sort_by(self):
        if 'sort_by' not in self.request.GET:
            self.request.GET['sort_by'] = self.default_sort_by
        sort_by = self.request.GET.get('sort_by', self.default_sort_by)
        if sort_by not in self.sort_by and (sort_by[1:] not in self.sort_by or sort_by[0] != '-'):
            sort_by = self.default_sort_by
        return sort_by
