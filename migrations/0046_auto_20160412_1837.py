# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0045_auto_20160412_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.IntegerField(choices=[(1, 'W trakcie realizacji'), (2, 'Projekt przerwano'), (3, 'Projekt zako\u0144czono')], default=1),
        ),
    ]
