# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'services/images/2b1b8c68/', verbose_name='image'),
        ),
    ]
