# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 01:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0052_auto_20160418_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=datetime.datetime(2016, 4, 18, 1, 1, 3, 475420, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
