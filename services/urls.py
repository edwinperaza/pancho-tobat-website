from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ServiceListView.as_view(),
        name='service_list_view'),
    url(r'^(?P<slug>[\w-]+)-(?P<pk>\d+)/$',
        views.ServiceDetailView.as_view(),
        name='service_detail_view'),
]
