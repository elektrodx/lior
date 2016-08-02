# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_qtystock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qtystock',
            name='qtyf',
        ),
    ]
