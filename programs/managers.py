from django.db import models


class ProgramManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return self.get_queryset().filter(is_active=True)


class ImageManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return self.get_queryset().filter(is_active=True)
