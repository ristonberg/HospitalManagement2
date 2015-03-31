# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0011_remove_myuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 3, 26)),
            preserve_default=True,
        ),
    ]
