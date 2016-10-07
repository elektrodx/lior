# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20160730_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_min', models.DecimalField(max_digits=6, decimal_places=2)),
                ('price_est', models.DecimalField(max_digits=6, decimal_places=2)),
                ('price_fac', models.DecimalField(max_digits=6, decimal_places=2)),
                ('price_sfac', models.DecimalField(max_digits=6, decimal_places=2)),
                ('state', models.BooleanField(default=True)),
                ('item', models.ForeignKey(to='stock.Stock')),
            ],
        ),
    ]
