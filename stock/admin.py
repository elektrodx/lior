from django.contrib import admin
from .models import *
from user_lior.models import Sucursal

class StockAdmin(admin.ModelAdmin):
	list_display = ('brand', 'qty', 'description', 'code', 'date_end', 'price_base', 'units', 'place', 'note')

admin.site.register(Stock, StockAdmin)

class UnitAdmin(admin.ModelAdmin):
	list_display = ('unit',)

admin.site.register(Unit, UnitAdmin)
