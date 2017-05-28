# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from base.models import BaseModel


class Program(BaseModel):
    name = models.CharField(
        _('name'),
        blank=True,
        max_length=100,
    )
    description = models.TextField(_('description'))
    order = models.PositiveIntegerField(_('order'), default=0)
