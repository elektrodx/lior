from django.db import models

class Providers(models.Model):
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	fono = models.CharField(max_length=15)
	account = models.CharField(max_length=50, blank=True, null=True)
	bank_account = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=150)
	def __unicode__(self):
		return self.name

class Customers(models.Model):
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=250, blank=True, null=True)
	fono = models.CharField(max_length=15, blank=True, null=True)
	ci = models.CharField(max_length=12, blank=True, null=True)
	def __unicode__(self):
		return self.name