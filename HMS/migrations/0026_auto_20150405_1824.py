# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0025_auto_20150405_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.BooleanField(choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')]),
            preserve_default=True,
        ),
    ]
