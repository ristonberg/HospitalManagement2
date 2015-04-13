# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0011_remove_myuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(verbose_name='e-mail', max_length=255, unique=True),
            preserve_default=True,
        ),
    ]
