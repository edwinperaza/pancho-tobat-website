from django.conf.urls import patterns, url

urlpatterns = patterns('nicolleknust.apps.contacts.views',
	url(r'^$', 'contact_form_view', name='contact_form_view'),
)
