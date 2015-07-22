# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('user_lior', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relations', '0002_auto_20150721_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('price_extra', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('total_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('payed', models.DecimalField(max_digits=6, decimal_places=2)),
                ('pay_due', models.DateField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('provider', models.ForeignKey(to='relations.Providers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField()),
                ('price_shop', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('item', models.ForeignKey(to='stock.Stock')),
                ('place', models.ForeignKey(to='user_lior.Sucursal')),
            ],
        ),
    ]
