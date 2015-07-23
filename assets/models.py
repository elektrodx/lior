from django.db import models
from relations.models import Providers, Customers

class Expenses(models.Model):
	date = models.DateField(auto_now_add=True)
	provider = models.ForeignKey(Providers)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	concept = models.CharField(max_length=100)
	note = models.TextField(blank=True, null=True)

class Income(models.Model):
	date = models.DateField(auto_now_add=True)
	customer = models.ForeignKey(Customers)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	concept = models.CharField(max_length=100)
	note = models.TextField(blank=True, null=True)

class Budget(models.Model):
	date_due = models.DateField()
	provider = models.ForeignKey(Providers)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	concept = models.CharField(max_length=100)
	note = models.TextField(blank=True, null=True)