# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0024_auto_20150405_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=7, choices=[('MAL', 'Male'), ('FEM', 'Female')], default=''),
            preserve_default=True,
        ),
    ]
