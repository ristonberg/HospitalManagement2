# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0042_auto_20150412_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name_plural': 'MyUsers', 'verbose_name': 'MyUser'},
        ),
        migrations.AlterModelOptions(
            name='nurse',
            options={'verbose_name': 'Nurse'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient'},
        ),
    ]
