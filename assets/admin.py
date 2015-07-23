from django.contrib import admin
from .models import *

class ExpensesAdmin(admin.ModelAdmin):
	list_display = ('date', 'provider', 'amount', 'concept', 'note')

admin.site.register(Expenses, ExpensesAdmin)

class IncomeAdmin(admin.ModelAdmin):
	list_display = ('date', 'customer', 'amount', 'concept', 'note')

admin.site.register(Income, IncomeAdmin)

class BudgetAdmin(admin.ModelAdmin):
	list_display = ('date_due', 'provider', 'amount', 'concept', 'note')

admin.site.register(Budget, BudgetAdmin)
