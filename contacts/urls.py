from django.conf.urls import url

from . import views

urlpatterns = [
    url(
      r'^$',
      views.ContactFormView.as_view(),
      name='contact_form_view'
    ),
]
