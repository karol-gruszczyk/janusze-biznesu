from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

from apps.shares import urls as shares_urls
from apps.stats import urls as stats_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/logout/$', views.logout, {'next_page': '/'}),
    url(r'', include(shares_urls, namespace='shares')),
    url(r'^stats/', include(stats_urls, namespace='stats')),
]
