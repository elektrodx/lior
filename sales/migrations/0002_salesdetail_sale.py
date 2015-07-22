# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdetail',
            name='sale',
            field=models.ForeignKey(default=1, to='sales.Sales'),
            preserve_default=False,
        ),
    ]
