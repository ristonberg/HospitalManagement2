# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0017_auto_20150404_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='marital_Status',
            field=models.CharField(choices=[('SIN', 'Single'), ('MAR', 'Married')], max_length=10, default=''),
            preserve_default=True,
        ),
    ]
