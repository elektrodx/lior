# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20160712_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='parts_left',
            field=models.IntegerField(default=0),
        ),
    ]
