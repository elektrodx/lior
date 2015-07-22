# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='email',
            field=models.EmailField(max_length=100, null=True, blank=True),
        ),
    ]
