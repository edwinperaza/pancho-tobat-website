# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(
        _('name'),
        max_length=100,
    )
    email = models.EmailField(
        _('email'),
        max_length=100,
    )
    phone = models.CharField(
        _('phone'),
        max_length=100,
        null=True,
    )
    message = models.TextField(
        _('message'),
    )

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.email)

    def clean(self):
        self.name = self.name.title().strip()
        self.email = self.email.strip()
        self.message = self.message.strip()
