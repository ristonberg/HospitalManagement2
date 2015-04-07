# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0018_auto_20150404_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='state',
        ),
    ]
