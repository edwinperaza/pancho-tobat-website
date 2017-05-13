from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^contact/', include('contacts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
