# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0007_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default=datetime.date(2016, 2, 28), upload_to=b'/home/dawid/django_tango/static/images/Python.png', verbose_name=b'png'),
            preserve_default=False,
        ),
    ]
