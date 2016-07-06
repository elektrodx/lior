# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='parts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='parts_left',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='price_by_parts',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
