from django.views.generic import ListView, DetailView
from .models import Service


class ServiceListView(ListView):
    model = Service

    def get_queryset(self):
        return Service.objects.active()


class ServiceDetailView(DetailView):
    model = Service

    def get_queryset(self):
        return Service.objects.active()
