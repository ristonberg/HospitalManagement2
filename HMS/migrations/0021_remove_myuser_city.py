# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0020_auto_20150405_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='city',
        ),
    ]
