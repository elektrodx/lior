from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
	list_display = ('pk','date','provider','user','price_extra','total_price','payed','pay_due','note',)

admin.site.register(Shop, ShopAdmin)

class ShopDetailAdmin(admin.ModelAdmin):
	list_display = ('shop', 'item','qty','place','price_shop','note',)

admin.site.register(ShopDetail, ShopDetailAdmin)