from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import UnitForm
from .forms import StockForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from templatetags.urlgen import urlGen
from django.template import RequestContext

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

@login_required(login_url="/singin")
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
	qty = len(q_stock)
	sumstock = 0
	for index in q_stock:
		if index.parts <> 0:
			sumstock = sumstock + (index.qty*index.price_base) + (index.price_by_parts*index.parts_left)
		else:
			sumstock = sumstock + (index.qty*index.price_base)
	return render(request, 'detail_stock.html', locals())

@login_required(login_url="/singin")
def detail_stock_pag(request):
	q_stock = Stock.objects.all()
	qty = len(q_stock)
	sumstock = 0
	for index in q_stock:
		if index.parts <> 0:
			sumstock = sumstock + (index.qty*index.price_base) + (index.price_by_parts*index.parts_left)
		else:
			sumstock = sumstock + (index.qty*index.price_base)

	items = q_stock.count()
	paginado = Paginator(q_stock, 21)
	print paginado.num_pages

	# Make sure page request is an int. If not, deliver first page.
	try:
	    page = int(request.GET.get('page', '1'))
	except ValueError:
	    page = 1

	#page = request.GET.get ('page')
	try:
		stock_pag = paginado.page(page)
	except PageNotAnInteger:
		stock_pag = paginado.page(1)
	except (EmptyPage, InvalidPage):
		stock_pag = paginado.page(paginado.num_pages)
		page = paginado.num_pages

###
	url = urlGen()
	pageURI = url.generate('page', request.GET)
	stock_pag = stock_pag.object_list

	return render_to_response('detail_stock_pag.html', {'stock_pag': stock_pag,
											'qty': qty,
											'sumstock': sumstock,
											'total_item': items,
											'pageURI': pageURI,
											'current': page
											}, context_instance=RequestContext(request))

###
###	return render (request, 'detail_stock_pag.html', locals())

@login_required(login_url="/singin")
def search_stock(request):
	form = StockForm()
	if request.method == "POST":
		form = StockForm(request.POST)
		message = request.POST.get('description')
		print(message)
		q_stock = Stock.objects.filter(description__icontains = message)
		if len(q_stock) == 0:
			mess_split = message.split(' ')
			q_stock = Stock.objects.filter(code__icontains = mess_split[0])
		return render(request, 'searched_stock.html', locals())
	else:
		form = StockForm()
	return render(request, 'search_stock.html', {'form': form })

@login_required(login_url="/singin")
def add_price(request):
	if request.method == "POST":
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/detail_stock_pag')
	else:
		form = StockForm()
	return render(request, 'add_price.html', {'form': form })