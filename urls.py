from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

from apps.shares import urls as shares_urls
from apps.shares import api_urls as shares_api_urls
from apps.stats import urls as stats_urls
from apps.updater import urls as updater_urls
from apps.tasks import urls as tasks_urls
from apps.gains import urls as gains_urls
from apps.correlations import urls as correlations_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^accounts/login/$', views.login),
    url(r'^accounts/logout/$', views.logout, {'next_page': '/'}),

    # applications
    url(r'^$', include(gains_urls, namespace='gains')),
    url(r'^shares/', include(shares_urls, namespace='shares')),
    url(r'^api/', include(shares_api_urls, namespace='api-shares')),
    url(r'^updater/', include(updater_urls, namespace='updater')),
    url(r'^stats/', include(stats_urls, namespace='stats')),
    url(r'^tasks/', include(tasks_urls, namespace='tasks')),
    url(r'^correlations/', include(correlations_urls, namespace='correlations')),
]
