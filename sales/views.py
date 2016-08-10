from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from home.views import home
from relations.models import Customers
from stock.models import Stock
from assets.models import Income
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import os, json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, JsonResponse
import datetime
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

def report_sale(request):
  context = 'hola'
  return render(request, 'report_sale.html', {'context': context})

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
      # pdb.set_trace()
      for index in data:
        itempk = Stock.objects.get(code=index[0])
        itempk.qty = itempk.qty - int(index[3])
        if int(index[6])>0:
          if itempk.parts_left==0:
            itempk.parts_left=itempk.parts
          itempk.qty = itempk.qty - 1  
          itempk.parts_left=itempk.parts_left-int(index[6])  
        itempk.save()
        saledetail = SalesDetail(sale_id=int(lastsale.pk), item_id=int(itempk.pk), qty=int(index[3]), place_id=1, price=float(index[4]), qtyf=int(index[6]), pricef=float(index[7]))
        saledetail.save()
      return HttpResponse(status=201)

def invoice(request):
    saleL = Sales.objects.last()
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invoice.pdf"'
    items = SalesDetail.objects.filter(sale__pk=saleL.pk)
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setPageSize(landscape(letter))
    p.setFont("Courier", 18)
    p.drawString(50, 550, "Dental Lior")
    p.drawString(420, 550, "Dental Lior")
    p.setFont("Courier", 12)
    p.drawString(300, 550, saleL.date.strftime("%d-%b-%Y"))
    p.drawString(670, 550, saleL.date.strftime("%d-%b-%Y"))
    p.drawString(300, 535, "Recibo N. "+str(saleL.pk))
    p.drawString(670, 535, "Recibo N. "+str(saleL.pk))
    p.drawString(50,535, "Nombre: " + saleL.customer.name)
    p.drawString(420, 535, "Nombre: " + saleL.customer.name)
    p.setFont('Courier', 22)
    p.drawString(120, 500, "Nota de Venta")
    p.drawString(490, 500, "Nota de Venta")
    p.line(50, 480, 380, 480)
    p.line(420, 480, 750, 480)
    p.setFont("Courier-Bold", 8)
    p.drawString(50, 460, "Codigo")
    p.drawString(110, 460, "Descripcion")
    p.drawString(220, 460, "Cant.")
    p.drawString(250, 460, "Prec.")
    p.drawString(280, 460, "Frac.")
    p.drawString(310, 460, "P.Frac")
    p.drawString(350, 460, "Total")
    p.drawString(420, 460, "Codigo")
    p.drawString(480, 460, "Descripcion")
    p.drawString(590, 460, "Cant.")
    p.drawString(620, 460, "Prec.")
    p.drawString(650, 460, "Frac.")
    p.drawString(680, 460, "P.Frac")
    p.drawString(720, 460, "Total")
    y=440
    p.setFont("Courier", 6)
    for index in items:
      p.drawString(50, y, index.item.code)
      p.drawString(110, y, index.item.brand + " " + index.item.description)
      p.drawString(220, y, str(index.qty))
      p.drawString(250, y, str(index.price))
      p.drawString(280, y, str(index.qtyf))
      p.drawString(310, y, str(index.pricef))
      p.drawString(350, y, str((index.qty*index.price)+(index.qtyf*index.pricef)))
      p.drawString(420, y, index.item.code)
      p.drawString(480, y, index.item.brand + " " + index.item.description)
      p.drawString(590, y, str(index.qty))
      p.drawString(620, y, str(index.price))
      p.drawString(650, y, str(index.qtyf))
      p.drawString(680, y, str(index.pricef))
      p.drawString(720, y, str((index.qty*index.price)+(index.qtyf*index.pricef)))
      y = y - 10
    p.line(50,70,380,70)
    p.line(420, 70, 750,70)
    p.drawString(50, 80, "Cantidad de Productos: " + str(len(items)))
    p.drawString(420, 80, "Cantidad de Productos: " + str(len(items)))
    p.setFont("Courier-Bold", 12)
    p.drawString(230, 55, "Total a Pagar: " + str(saleL.amount))
    p.drawString(600, 55, "Total a Pagar: " + str(saleL.amount))
    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
