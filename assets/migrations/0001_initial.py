# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_auto_20150721_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_due', models.DateField()),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('concept', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('provider', models.ForeignKey(to='relations.Providers')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('concept', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('provider', models.ForeignKey(to='relations.Providers')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('concept', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('customer', models.ForeignKey(to='relations.Customers')),
            ],
        ),
    ]
