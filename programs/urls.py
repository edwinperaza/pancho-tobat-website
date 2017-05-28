from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ProgramListView.as_view(),
        name='program_list_view'),
    url(r'^(?P<slug>[\w-]+)-(?P<pk>\d+)/$',
        views.ProgramDetailView.as_view(),
        name='program_detail_view'),
]
