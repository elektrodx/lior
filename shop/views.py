from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from relations.models import Providers
from assets.models import Expenses
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import pdb, ast

@login_required(login_url="/singin")
def add_shop(request):
	if request.method == "POST":
		form = ShopForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ShopForm()
	return render(request, 'add_shop.html', {'form': form })

@csrf_exempt
def shop_add(request):
	if request.is_ajax:
		user = request.user.pk
		provider = int(request.POST.get('provider'))
		price_extra = float(request.POST.get('price_extra'))
		total_price = float(request.POST.get('total_price'))
		shopn = Shop()
		shopn.date = datetime.now()
		shopn.provider_id=provider
		shopn.user_id=int(user)
		shopn.price_extra=price_extra
		shopn.total_price=total_price
		shopn.payed = total_price + price_extra
		shopn.save()
		expensesN = Expenses(provider_id=provider, amount=total_price+price_extra, concept='Compra de Productos')
		expensesN.save()
		items = request.POST.dict()
		data = ast.literal_eval(items['items'])
		lastshop = Shop.objects.last()
		for index in data:
			item_pk = Stock.objects.get(code=index[0])
			item_pk.qty = item_pk.qty + int(index[2])
			if item_pk.price_base < float(index[5]):
				item_pk.price_base = float(index[5])
			item_pk.save()	
			item_qty = int(index[2])
			item_price_shop = float(index[5])
			shop_detailN = ShopDetail(shop_id=lastshop.pk, item_id=item_pk.pk, qty=item_qty, place_id=1, price_shop=item_price_shop)
			shop_detailN.save()
		return HttpResponse(status=201)
	else:			
		return HttpResponse(status=501)

