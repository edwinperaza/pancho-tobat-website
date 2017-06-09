from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Program, Image


class ImageAdminInline(admin.TabularInline):
    model = Image
    max_num = 1
    exclude = ('order', 'is_active',)


@admin.register(Program)
class ProgramAdmin(SummernoteModelAdmin):
    list_display = ('name', 'order', 'is_active',)
    list_filter = ('is_active',)
    inlines = [ImageAdminInline]

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        js = (
            'js/tiny_mce/tiny_mce.js',
            'js/tiny_mce/textareas.js',
        )


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('service', 'order', 'is_active',)
#     list_filter = ('is_active',)
