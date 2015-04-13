# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0035_auto_20150409_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
