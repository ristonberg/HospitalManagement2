# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=255, verbose_name='email address', unique=True)),
                ('first_name', models.CharField(max_length=20, default='')),
                ('last_name', models.CharField(max_length=20, default='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_content_manager', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('department', models.CharField(max_length=30, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('HMS.myuser',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True)),
                ('specialty', models.CharField(max_length=40, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('HMS.myuser',),
        ),
    ]
