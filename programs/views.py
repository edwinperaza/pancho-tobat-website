from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from .models import Program


class ProgramListView(ListView):
    model = Program

    def get_queryset(self):
        return Program.objects.active()


class ProgramDetailView(DetailView):
    model = Program

    def get_queryset(self):
        return Program.objects.active()


class ProgramDetailRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        program = get_object_or_404(Program, pk=kwargs['pk'])
        return program.get_absolute_url()
