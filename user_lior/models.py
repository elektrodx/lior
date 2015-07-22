from django.db import models
from django.contrib.auth.models import User

class Sucursal(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Users_lior(models.Model):
	user_user = models.OneToOneField(User, primary_key=True)
	fono = models.CharField(max_length=15)
	sucursal = models.ForeignKey(Sucursal)



