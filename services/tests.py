from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from .models import Service


def create_service(name='foo', description='bar', **kwargs):
    return Service.objects.create(name=name, description=description, **kwargs)


class ServiceListView(TestCase):

    def setUp(self):
        self.url = reverse('service_list_view')
        self.service = create_service()
        self.service2 = create_service(is_active=False)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'services/service_list.html')

    def test_active_list_service(self):
        response = self.client.get(self.url)
        self.assertIn(self.service, response.context['service_list'])
        self.assertNotIn(self.service2, response.context['service_list'])


class ServiceDetailView(TestCase):

    def setUp(self):
        self.service = create_service()
        self.url = self.service.get_absolute_url()  # reverse('service_detail_view', kwargs={'slug': slugify(self.service.name), 'pk': self.service.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'services/service_detail.html')

    def test_active(self):
        self.service.is_active = False
        self.service.save()
        response = self.client.get(self.url)
        self.assertEqual(404, response.status_code)
