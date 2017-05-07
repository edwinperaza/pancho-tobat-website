from django.conf.urls import patterns, url


urlpatterns = patterns('mandu.apps.services.views',
    url(r'^$', 'service_list_view', name='service_list_view'),
    url(r'^(?P<slug>[\w-]+)-(?P<pk>\d+)/$', 'service_detail_view', name='service_detail_view'),
)
