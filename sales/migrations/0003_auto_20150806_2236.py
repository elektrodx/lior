# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_salesdetail_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
