from django.views.generic import TemplateView


from contacts.forms import ContactForm
from services.models import Service


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = ContactForm
        context['services'] = Service.objects.active()
        return context
