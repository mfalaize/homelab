# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compta', '0007_identifiant_encrypted'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='solde_en_une_fois',
            field=models.BooleanField(default=False, verbose_name='Soldé en une fois'),
        ),
        migrations.AlterField(
            model_name='identifiant',
            name='encrypted',
            field=models.BooleanField(default=False, verbose_name='Le mot de passe a été crypté'),
        ),
    ]
