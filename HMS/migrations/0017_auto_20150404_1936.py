# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0016_auto_20150404_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
            preserve_default=True,
        ),
    ]
