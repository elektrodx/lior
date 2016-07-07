# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20160705_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='price_by_parts',
        ),
    ]
