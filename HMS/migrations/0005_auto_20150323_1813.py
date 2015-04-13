# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0004_auto_20150323_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.CharField(default='', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.CharField(default='', max_length=20),
            preserve_default=True,
        ),
    ]
