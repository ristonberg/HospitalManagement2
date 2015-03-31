# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0017_auto_20150330_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 3, 31)),
            preserve_default=True,
        ),
    ]
