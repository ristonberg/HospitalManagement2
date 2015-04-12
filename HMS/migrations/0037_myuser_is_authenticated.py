# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0036_auto_20150409_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_authenticated',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
