# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0032_auto_20160322_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_choices', models.IntegerField(choices=[(1, b'Styczen'), (2, b'Luty'), (3, b'Marzec'), (4, b'Kwiecien')], default=1)),
            ],
        ),
    ]
