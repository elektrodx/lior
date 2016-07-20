from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from home.views import home
from relations.models import Customers
from stock.models import Stock
from assets.models import Income
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
import os, json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, JsonResponse
import pdb, ast

@login_required(login_url="/singin")
def add_sale(request):
	if request.method == "POST":
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = SalesForm()
	return render(request, 'add_sale.html', {'form': form })

class Invoice(PDFTemplateView):
    template='invoice.html'
    q_sales = Sales.objects.all().last()
    d_sales = SalesDetail.objects.filter(sale=q_sales.pk)
    context = { 'pk': q_sales.pk, 'customer': q_sales.customer, 'date': q_sales.date, 'total': q_sales.amount, 'items': d_sales }
    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="hello.pdf",
                                       context= self.context,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 5,
                                       'orientation': 'Landscape',
                                       'page-size': 'Letter'},
                                       )
        return response

@csrf_exempt
def sales_postjson(request):
  if request.method == 'POST':
    if request.is_ajax():
      data = request.body
      return data
    s = Sales()
    s.amount = data.amount
    s.save()
    return render(request,'home.html')

def list_customer(request):
  q_stock = Customers.objects.all()
  data = [{'id': item.id, 'name': item.name, 'address': item.email, 'fono': item.fono, 'ci': item.ci, } for item in q_stock ]
  return JsonResponse(data, safe=False)

@csrf_exempt
def sale_add(request):
    if request.is_ajax:
      user = request.user.pk
      amount = float(request.POST.get('amount'))
      # pay_date = request.POST.get('pay_date')
      customerdni = request.POST.get('customer')
      items = request.POST.dict()
      customer = Customers.objects.get(ci=customerdni)
      sale = Sales(user_id=user, amount=amount, payed=amount, customer_id=customer.pk)
      sale.save()
      incomen = Income(customer_id=customer.pk, amount=amount, concept="ventas")
      incomen.save()
      data = ast.literal_eval(items['items'])
      lastsale = Sales.objects.last()
      for index in data:
        itempk = Stock.objects.get(code=index[0])
        itempk.qty = itempk.qty - int(index[3])
        itempk.save()
        saledetail = SalesDetail(sale_id=int(lastsale.pk), item_id=int(itempk.pk), qty=int(index[3]), place_id=1, price=float(index[4]))
        saledetail.save()  
      return HttpResponse(status=201)

