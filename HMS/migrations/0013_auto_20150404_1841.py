# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0012_auto_20150404_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='department',
            field=models.CharField(default='', max_length=30, choices=[('PED', 'Pediatrics'), ('ONC', 'Oncology')]),
            preserve_default=True,
        ),
    ]
