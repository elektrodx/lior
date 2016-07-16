# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_stock_price_by_parts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
