from django.views.generic import ListView, DetailView
from .models import Service


class ServiceListView(ListView):
    model = Service

    def get_queryset(self):
        return Service.objects.active()

service_list_view = ServiceListView.as_view()


class ServiceDetailView(DetailView):
    model = Service
    query_pk_and_slug = True

    def get_queryset(self):
        return Service.objects.active()

service_detail_view = ServiceDetailView.as_view()
