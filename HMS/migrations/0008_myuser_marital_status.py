# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0007_auto_20150323_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='marital_Status',
            field=models.CharField(max_length=10, default=''),
            preserve_default=True,
        ),
    ]
