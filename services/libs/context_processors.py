from django.core.cache import cache

from mandu.apps.services.models import Service


def service_list_menu(request):
    return {
        'service_list_menu': Service.objects.active().values('name')
    }
