from django.db import models
from django.contrib.auth.models import User
from relations.models import Customers
from stock.models import Stock
from user_lior.models import Sucursal

class Sales(models.Model):
	date = models.DateField(auto_now_add=False)
	customer = models.ForeignKey(Customers)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	payed = models.DecimalField(max_digits=6, decimal_places=2)
	pay_date = models.DateField(blank=True, null=True)
	user = models.ForeignKey(User)
	note = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return str(self.id)

class SalesDetail(models.Model):
	sale = models.ForeignKey(Sales)
	item = models.ForeignKey(Stock)
	qty = models.IntegerField()
	place = models.ForeignKey(Sucursal)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	note = models.TextField(blank=True, null=True)


