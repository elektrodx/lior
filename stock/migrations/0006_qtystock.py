# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_lior', '0001_initial'),
        ('stock', '0005_auto_20160730_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qtystock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=0)),
                ('qtyf', models.IntegerField(default=0)),
                ('price_base', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('parts_left', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('item', models.ForeignKey(to='stock.Stock')),
                ('place', models.ForeignKey(to='user_lior.Sucursal')),
            ],
        ),
    ]
