# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0028_auto_20160314_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paczki',
            name='p',
            field=models.FloatField(),
        ),
    ]