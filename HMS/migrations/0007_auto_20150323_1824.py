# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0006_auto_20150323_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(default='', max_length=7),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='primary_Phone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='relation',
            field=models.CharField(default='', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='secondary_Phone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
