from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UnitForm
from .forms import StockForm
from .models import Stock
from django.core import serializers

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
def add_stock(request):
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_stock')
	else:
		form = StockForm()
	return render(request, 'add_stock.html', {'form': form })

def list_stock(request):
	objectQuerySet = Stock.objects.all()
	#objectQuerySet = Stock.objects.filter(brand='Colgate')
	data = serializers.serialize('json', objectQuerySet, fields=('brand', 'code', 'date_end', 'qty', 'description', 'price_base', 'units', 'place', 'note',))
	return HttpResponse(data, content_type='application/json')

def detail_stock(request):
	q_stock = Stock.objects.all()
	return render(request, 'detail_stock.html', locals())
