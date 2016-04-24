from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from stock.models import Stock

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