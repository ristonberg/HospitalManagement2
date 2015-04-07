# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0029_auto_20150406_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='actor_type',
            field=models.CharField(default='', max_length=7, choices=[('DOC', 'DOCTOR'), ('PAT', 'PATIENT'), ('NUR', 'NURSE'), ('ADMIN', 'ADMIN')]),
            preserve_default=True,
        ),
    ]
