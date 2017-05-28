# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170513_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'services/images/6f53dd46/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='descripci\xf3n'),
        ),
    ]
