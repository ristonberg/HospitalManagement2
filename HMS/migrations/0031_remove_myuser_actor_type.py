# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0030_auto_20150406_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='actor_type',
        ),
    ]
