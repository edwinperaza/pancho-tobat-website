from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail
from django.template.loader import render_to_string

from django.contrib.auth.models import User
# from dressmoi.apps.users.tests import create_user

from .conf import settings
from .forms import ContactForm
from .models import Contact


class ContactViewTest(TestCase):

    def setUp(self):
        self.url = reverse('contact_form_view')

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')

    def test_get_type_param(self):
        response = self.client.get(self.url, {'kind': Contact.KIND_QUESTION})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')
        self.assertEqual(response.context['form'].initial['kind'], str(Contact.KIND_QUESTION))

    def test_get_email_param(self):
        user = User.objects.create_user('foo', 'bar', 'password')  # create_user(password='password')
        self.client.login(username=user.username, password='password')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')
        self.assertEqual(response.context['form'].initial['email'], user.email)

    def test_post(self):
        params = {
            'name': 'Foo',
            'email': 'admin@example.net',
            'phone': '123456',
            'body': 'Lorem ipsum dolor sit amet'
        }

        response = self.client.post(self.url, params)
        self.assertRedirects(response, self.url)

        contact = Contact.objects.get()
        self.assertEqual(params['name'], contact.name)
        self.assertEqual(params['email'], contact.email)
        self.assertEqual(params['phone'], contact.phone)
        self.assertEqual(params['body'], contact.body)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, settings.CONTACTS_EMAILS)
        self.assertEqual(email.from_email, contact.email)
        self.assertEqual(email.subject, render_to_string('contacts/email_contact_subject.txt',
                                                         {'contact': contact}))
        self.assertEqual(email.body, render_to_string('contacts/email_contact.txt',
                                                      {'contact': contact}))

    def test_get_ajax(self):
        response = self.client.get(self.url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/ajax/contact_form.html')
        self.assertTemplateNotUsed(response, 'contacts/contact_form.html')
