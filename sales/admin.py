from django.contrib import admin
from .models import *

class SalesAdmin(admin.ModelAdmin):
	list_display = ('date', 'customer', 'amount', 'payed', 'pay_date', 'user', 'note')

admin.site.register(Sales, SalesAdmin)

class SalesDetailAdmin(admin.ModelAdmin):
	list_display = ('sale', 'item', 'qty', 'place', 'price', 'note')

admin.site.register(SalesDetail, SalesDetailAdmin)