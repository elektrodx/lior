from django.contrib import admin
from .models import *

class ProvidersAdmin(admin.ModelAdmin):
	list_display = ('name','email','address','fono','account','bank_account','contact',)

admin.site.register(Providers, ProvidersAdmin)

class CustomersAdmin(admin.ModelAdmin):
	list_display = ('name','email','address','fono','ci',)

admin.site.register(Customers, CustomersAdmin)