from django.db import models
from django.contrib.auth.models import User
from relations.models import Providers
from stock.models import Stock
from user_lior.models import Sucursal

class Shop(models.Model):
	date = models.DateField()
	provider = models.ForeignKey(Providers)
	user = models.ForeignKey(User)
	price_extra = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	total_price = models.DecimalField(max_digits=6, decimal_places=2)
	payed = models.DecimalField(max_digits=6, decimal_places=2)
	pay_due = models.DateField(blank=True, null=True)
	note = models.TextField(blank=True, null=True)

class ShopDetail(models.Model):
	item = models.ForeignKey(Stock)
	qty = models.IntegerField()
	place = models.ForeignKey(Sucursal)
	price_shop = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	note = models.TextField(blank=True, null=True)
	