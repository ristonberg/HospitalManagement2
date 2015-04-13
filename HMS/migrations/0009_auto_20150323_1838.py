# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0008_myuser_marital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('medical_History', models.CharField(max_length=40, default='')),
                ('insurance_Provider', models.CharField(max_length=40, default='')),
                ('insurance_Policy_Number', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('HMS.myuser',),
        ),
        migrations.AddField(
            model_name='doctor',
            name='degree',
            field=models.CharField(max_length=40, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(max_length=60, default=''),
            preserve_default=True,
        ),
    ]
