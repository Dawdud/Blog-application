# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pavelstanlley', '0002_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='country',
        ),
    ]
