# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0017_auto_20160311_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpictures',
            name='image',
            field=models.ImageField(upload_to=b'post_images'),
        ),
    ]
