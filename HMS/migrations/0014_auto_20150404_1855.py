# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0013_auto_20150404_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='department',
            field=models.CharField(max_length=30, choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')], default=''),
            preserve_default=True,
        ),
    ]
