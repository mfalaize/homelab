# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 17:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compta', '0015_auto_20170812_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='contributeur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Contributeur'),
        ),
    ]
