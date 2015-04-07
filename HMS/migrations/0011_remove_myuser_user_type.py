# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0010_myuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_Type',
        ),
    ]
