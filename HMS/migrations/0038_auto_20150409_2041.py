# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0037_myuser_is_authenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_authenticated',
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_authenticated',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='is_authenticated',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='is_authenticated',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
