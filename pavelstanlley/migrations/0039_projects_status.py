# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 17:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0038_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(default=datetime.datetime(2016, 4, 11, 17, 15, 11, 890182, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
