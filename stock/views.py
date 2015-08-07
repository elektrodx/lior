from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UnitForm
from .forms import StockForm

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

def add_stock(request):
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_stock')
	else:
		form = StockForm()
	return render(request, 'add_stock.html', {'form': form })