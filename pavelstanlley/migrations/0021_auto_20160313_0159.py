# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0020_auto_20160313_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpictures',
            name='post',
            field=models.ManyToManyField(to='pavelstanlley.Post'),
        ),
    ]
