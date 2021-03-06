# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0041_auto_20150411_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 12)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 12)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nurse',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 12)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 12)),
            preserve_default=True,
        ),
    ]
