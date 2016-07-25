# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20150806_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdetail',
            name='pricef',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesdetail',
            name='qtyf',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
