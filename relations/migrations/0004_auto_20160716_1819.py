# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0003_auto_20160627_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='ci',
            field=models.CharField(unique=True, max_length=12),
        ),
    ]
