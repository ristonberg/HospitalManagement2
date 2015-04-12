# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0040_auto_20150411_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='doctor',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 11)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 11)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 11)),
            preserve_default=True,
        ),
    ]
