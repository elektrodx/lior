# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_auto_20150721_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='ci',
            field=models.CharField(max_length=12),
        ),
    ]
