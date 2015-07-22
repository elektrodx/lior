# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetail',
            name='shop',
            field=models.ForeignKey(default=1, to='shop.Shop'),
            preserve_default=False,
        ),
    ]
