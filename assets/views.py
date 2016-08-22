from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ExpensesForm
from .models import *

# Create your views here.

@login_required(login_url="/singin")
def add_expenses(request):
	if request.method == "POST":
		form = ExpensesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_expenses')
	else:
		form = ExpensesForm()
	return render(request, 'add_expenses.html', {'form': form })

# @login_required(login_url="/singin")
# def report_exp(request):
# 	q_stock = Stock.objects.all()
# 	qty = len(q_stock)
# 	sumstock = 0
# 	for index in q_stock:
# 		if index.parts <> 0:
# 			sumstock = sumstock + (index.qty*index.price_base) + (index.price_by_parts*index.parts_left)
# 		else:
# 			sumstock = sumstock + (index.qty*index.price_base)
# 	return render(request, 'detail_stock.html', locals())