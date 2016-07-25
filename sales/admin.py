from django.contrib import admin
from .models import *

class SalesAdmin(admin.ModelAdmin):
	list_display = ('pk','date', 'customer', 'amount', 'payed', 'pay_date', 'user', 'note')

admin.site.register(Sales, SalesAdmin)

class SalesDetailAdmin(admin.ModelAdmin):
	list_display = ('sale', 'item', 'qty', 'price', 'qtyf', 'pricef', 'place', 'note')

admin.site.register(SalesDetail, SalesDetailAdmin)