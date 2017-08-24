# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0006_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name=b'comments', default=1, to='pavelstanlley.Post'),
            preserve_default=False,
        ),
    ]
