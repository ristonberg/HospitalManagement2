# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
