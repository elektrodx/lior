from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UnitForm
from .forms import StockForm
from .models import *

@login_required(login_url="/singin")
def add_unit(request):
	if request.method == "POST":
		form = UnitForm(request.POST)
		if form.is_valid():
			unity = request.POST['unit']
			form.save()
			#return HttpResponseRedirect('/add_unit')
			return HttpResponse('<script type="text/javascript">window.opener.reloadMyDivUnits(); window.close();</script>')
	else:
		form = UnitForm()
	return render(request, 'add_unit.html', {'form': form })

@login_required(login_url="/singin")
def add_unit_2(request):
	if request.method == "POST":
		form = UnitForm(request.POST)
		if form.is_valid():
			unity = request.POST['unit']
			form.save()
			#return HttpResponseRedirect('/add_unit')
			return HttpResponse('<script type="text/javascript">window.opener.reloadMyDivUnits(); window.close();</script>')
	else:
		form = UnitForm()
	return render(request, 'add_unit_2.html', {'form': form })

@login_required(login_url="/singin")
def add_stock(request):
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_stock')
	else:
		form = StockForm()
	return render(request, 'add_stock.html', {'form': form })

def edit_stock(request, id): 
    item = get_object_or_404(Stock, code=id)
    form = StockForm(request.POST or None, instance=item)
    if form.is_valid():
          form.save()
          return redirect('detail_stock')
    return render(request, 'edit_stock.html', {'form': form}) 

def list_stock(request):
	q_stock = Stock.objects.all()
	data = [{'description': item.description, 'brand': item.brand, 'code': item.code, 'qty': item.qty, 'price': item.price_base, 'unit': item.units.unit, 'place': item.place.name, 'pk': item.pk, 'parts_left': item.parts_left, 'parts': item.parts } for item in q_stock ]
	return JsonResponse(data, safe=False)

@login_required(login_url="/singin")
def detail_stock(request):
	q_stock = Stock.objects.all()
	return render(request, 'detail_stock.html', locals())
