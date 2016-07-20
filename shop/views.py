from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from relations.models import Providers
from datetime import date
from django.contrib.auth.decorators import login_required
import pdb, ast

@login_required(login_url="/singin")
def add_shop(request):
	if request.method == "POST":
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ShopForm()
	return render(request, 'add_shop.html', {'form': form })

def shop_add(request):
	if request.is_ajax:
		date = date.today()
		user = request.user.pk
		provider = request.POST.get('provider')
		price_extra = request.POST.get('price_extra')
		total_price = request.POST.get('total_price')
		items = request.POST.dict()
		pdb.set_trace()
		return


