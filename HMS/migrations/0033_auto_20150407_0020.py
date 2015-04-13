# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0032_auto_20150406_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='department',
            field=models.CharField(choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')], default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='degree',
            field=models.CharField(choices=[('MD', 'M.D.'), ('DO', 'D.O.')], default='MD', max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2015, 4, 7)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 7)),
            preserve_default=True,
        ),
    ]
