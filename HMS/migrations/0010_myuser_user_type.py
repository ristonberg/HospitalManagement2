# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0009_auto_20150323_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_Type',
            field=models.CharField(default='', max_length=10),
            preserve_default=True,
        ),
    ]
