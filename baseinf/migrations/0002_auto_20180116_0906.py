# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseinf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='city_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='country_id',
        ),
    ]