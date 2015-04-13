# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0031_remove_myuser_actor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_doctor',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nurse',
            name='is_nurse',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='is_patient',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
