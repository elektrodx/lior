# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=250, null=True, blank=True)),
                ('fono', models.CharField(max_length=15, null=True, blank=True)),
                ('ci', models.CharField(max_length=12, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=250, null=True, blank=True)),
                ('fono', models.CharField(max_length=15)),
                ('account', models.CharField(max_length=50, null=True, blank=True)),
                ('bank_account', models.CharField(max_length=50, null=True, blank=True)),
                ('contact', models.CharField(max_length=150)),
            ],
        ),
    ]
