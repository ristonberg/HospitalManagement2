# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0022_auto_20150405_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='zip_Code',
            new_name='zip_code',
        ),
    ]
