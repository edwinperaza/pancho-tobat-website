from django.views.generic import ListView, DetailView
from .models import Program


class ProgramListView(ListView):
    model = Program

    def get_queryset(self):
        return Program.objects.active()


class ProgramDetailView(DetailView):
    model = Program

    def get_queryset(self):
        return Program.objects.active()
