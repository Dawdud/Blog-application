# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0050_auto_20160414_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='projectimage',
        ),
    ]