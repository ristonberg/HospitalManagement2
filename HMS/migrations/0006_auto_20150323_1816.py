# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0005_auto_20150323_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='street_name',
            new_name='street',
        ),
        migrations.AddField(
            model_name='myuser',
            name='zip_Code',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
