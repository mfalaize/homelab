# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compta', '0018_auto_20170818_2329'),
    ]

    operations = [
        migrations.RunSQL("UPDATE compta_operation SET recette_id = NULL")
    ]