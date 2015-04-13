# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0028_auto_20150406_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='actor_type',
            field=models.CharField(choices=[('DOC', 'DOCTOR'), ('PAT', 'PATIENT'), ('NUR', 'NURSE'), ('ADMIN', 'ADMIN')], max_length=7, default='DOC'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology'), ('FAM', 'Family Practice'), ('EME', 'Emergency'), ('ORT', 'Orthopedics')], max_length=30, default=''),
            preserve_default=True,
        ),
    ]
