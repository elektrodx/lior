from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_user', 'fono', 'sucursal')

admin.site.register(Users_lior, UserAdmin)

class SucursalAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Sucursal, SucursalAdmin)