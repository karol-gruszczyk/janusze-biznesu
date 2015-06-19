from django.conf.urls import url, patterns

from .views import root

urlpatterns = patterns(
    '',
    url(r'^$', root),
)