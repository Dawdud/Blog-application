# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 02:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0023_auto_20160313_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pavelstanlley.Post'),
            preserve_default=False,
        ),
    ]
