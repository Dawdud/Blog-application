# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0048_auto_20160414_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[(b'CONCEPTION', 'pomys\u0142 projektu'), (b'IN_PROGRESS', 'W trakcie realizacji'), (b'BREAK', 'Projekt przerwano'), (b'END', 'Projekt zako\u0144czono')], default=0, max_length=50),
        ),
    ]