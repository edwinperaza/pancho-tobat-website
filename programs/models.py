from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from base.models import BaseModel, upload_to
from sorl.thumbnail import get_thumbnail

from .managers import ImageManager, ProgramManager


class Program(BaseModel):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    order = models.PositiveIntegerField(_('order'), default=0)
    is_active = models.BooleanField(_('is active'), default=True)

    objects = ProgramManager()

    class Meta:
        ordering = ('order', 'name',)

    def __unicode__(self):
        return self.name

    @property
    def image(self):
        image = self.images.active().first() if self.images.count() else None
        return image

    def get_absolute_url(self):
        return reverse(
            'program_detail_view',
            kwargs={'slug': slugify(self.name), 'pk': self.pk}
        )


class Image(BaseModel):
    program = models.ForeignKey(
        Program,
        verbose_name=_('program'),
        blank=False,
        null=True,
        related_name='images',
    )
    image = models.ImageField(
        _('image'),
        upload_to=upload_to('programs/images/'),
        )
    description = models.TextField(
        _('description'),
        null=True,
        blank=True,
        editable=False,
    )
    order = models.PositiveIntegerField(
        _('order'),
        default=0,
    )
    is_active = models.BooleanField(
        _('is active'),
        default=True,
    )

    objects = ImageManager()

    class Meta:
        ordering = ('order',)

    @property
    def image_list_horizontal(self):
        image = get_thumbnail(self.image, '470x148', crop='center')
        return image.url

    @property
    def image_detail(self):
        image = get_thumbnail(self.image, '400x280', crop='center')
        return image.url

    @property
    def image_detail_first(self):
        image = get_thumbnail(self.image, '470x360', crop='center')
        return image.url

    @property
    def image_gallery(self):
        image = get_thumbnail(self.image, '220x147', crop='center')
        return image.url

    @property
    def image_gallery_list(self):
        image = get_thumbnail(self.image, '303x202', crop='center')
        # image = get_thumbnailer(self.image)['service_list']
        return image.url
