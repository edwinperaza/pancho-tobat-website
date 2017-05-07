from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        return False
