from django.contrib import admin

from .models import Service, Image


class ImageAdminInline(admin.TabularInline):
    model = Image


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active',)
    list_filter = ('is_active',)
    inlines = [ImageAdminInline]

    class Media:
        js = (
            'js/tiny_mce/tiny_mce.js',
            'js/tiny_mce/textareas.js',
        )


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('service', 'order', 'is_active',)
#     list_filter = ('is_active',)
