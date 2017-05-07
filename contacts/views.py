# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Contact
from .forms import ContactForm


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class ContactFormView(AjaxableResponseMixin, CreateView):
    model = Contact
    form_class = ContactForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ContactFormView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        template_names = super(ContactFormView, self).get_template_names()
        if self.request.is_ajax():
            template_names.insert(0, 'contacts/ajax/contact_form.html')
        return template_names

    def get_success_url(self, instance=None):
        messages.success(
            self.request, _(u'Su Consulta Se Ha Enviado Con Éxito'))
        return reverse('contact_form_view')


contact_form_view = ContactFormView.as_view()
