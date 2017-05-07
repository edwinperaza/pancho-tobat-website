""" Admin base configuration """

# django
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.views.decorators.cache import never_cache


# standard library
import csv


class AdminSite(admin.sites.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = _('My site admin')

    # Text to put in each page's <h1>.
    site_header = _('My administration')

    # Text to put at the top of the admin index page.
    index_title = _('Site administration')


admin.site = AdminSite()


def download_report(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    queryset = queryset.select_related()
    data = queryset.values()
    writer.writerow(data[0].keys())

    for datum in data:
        writer.writerow([unicode(s).encode("utf-8") for s in datum.values()])

    return response


download_report.short_description = _("Download Data")
