from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from stock.models import Stock
from sales.models import Sales
from sales.models import SalesDetail
import os, json
from django.conf import settings

def list_stock_2(request):
	q_stock = Stock.objects.all()
	data = [{'description': item.description, 'brand': item.brand, 'code': item.code, 'qty': item.qty, 'price': item.price_base, 'unit': item.units.unit, 'place': item.place.name, 'pk': item.pk } for item in q_stock ]
	return JsonResponse(data, safe=False)

def list_code(request, codegen):
	q_stock = Stock.objects.filter(code__contains = codegen)
	data = [{'description': item.description, 'code': item.code, 'pk': item.pk } for item in q_stock ]
	return JsonResponse(data, safe=False)

def list_desc(request, codi):
	#request = descrip
	q_stock = Stock.objects.filter(code = codi)
	data = [{'description': item.description } for item in q_stock ]
	return JsonResponse(data, safe=False)

def list_sales(request):
	q_stock = Sales.objects.all()
	data = [{'id': item.id, 'date': item.date, 'amount': item.amount, 'payed': item.payed, 'pay_date': item.pay_date, 'note': item.note, 'customer_id': item.customer_id, 'user_id': item.user_id} for item in q_stock ]
	return JsonResponse(data, safe=False)

def list_detail_sale(request, code_sale):
	#code_sale = 4
	q_stock = SalesDetail.objects.filter(sale_id = code_sale)
	data = [{'id': item.id, 'qty': item.qty, 'price': item.price, 'note': item.note, 'item_id': item.item_id, 'place_id': item.place_id, 'sale_id': item.sale_id} for item in q_stock ]
	return JsonResponse(data, safe=False)

def json_sales(request):
	path = "{0}/jsons/sale.json".format(settings.STATIC_ROOT)
	with open(path, 'r') as f:
		sales_data = json.load(f)
	return render(request, 'json_sales.html', locals())

def json_sale_d(request, code_sale_d):
	pre_path = "{0}/jsons/sale"+code_sale_d+".json"
	path = pre_path.format(settings.STATIC_ROOT)
	with open(path, 'r') as f:
		sales_data = json.load(f)
	return render(request, 'json_sales.html', locals())