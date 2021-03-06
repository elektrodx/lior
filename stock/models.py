from django.db import models
from user_lior.models import Sucursal

class Unit(models.Model):
	unit = models.CharField(max_length=50)
	def __unicode__(self):
		return self.unit

class Stock(models.Model):
	brand = models.CharField(max_length=50)
	code = models.CharField(unique=True, max_length=50)
	date_end = models.DateField(blank=True, null=True)
	qty = models.IntegerField()
	parts = models.IntegerField(default=0)
	parts_left = models.IntegerField(default=0)
	description = models.CharField(max_length=200)
	price_base = models.DecimalField(max_digits=6, decimal_places=2)
	units = models.ForeignKey(Unit)
	place = models.ForeignKey(Sucursal)
	note = models.TextField(blank=True, null=True)
	def __unicode__(self):
		#return self.description
		#return "{0}".format(self.description, self.brand,)
		#return '%s %s' % (self.code, self.description,) 
		#return "{0} {1}".format(self.description, self.brand)
		return "{0} {1}".format(self.code, self.description)
	@property
	def total_price(self):
		return self.qty * self.price_base

	@property
	def price_by_parts(self):
		return self.price_base / self.parts

class Prices(models.Model):
	item = models.ForeignKey(Stock)
	price_min = models.DecimalField(max_digits=6, decimal_places=2)
	price_est = models.DecimalField(max_digits=6, decimal_places=2)
	price_fac = models.DecimalField(max_digits=6, decimal_places=2)
	price_sfac = models.DecimalField(max_digits=6, decimal_places=2)
	state = models.BooleanField(default=True)