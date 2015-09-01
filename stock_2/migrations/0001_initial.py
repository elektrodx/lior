# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_lior', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('date_end', models.DateField(null=True, blank=True)),
                ('qty', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('price_base', models.DecimalField(max_digits=6, decimal_places=2)),
                ('note', models.TextField(null=True, blank=True)),
                ('place', models.ForeignKey(to='user_lior.Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='units',
            field=models.ForeignKey(to='stock.Unit'),
        ),
    ]
