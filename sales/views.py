from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
import os, json
from django.conf import settings

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

def add_sale_d(request, code_sale_d):
  #if request.method == "POST":
  pre_path = "{0}/jsons/sale"+code_sale_d+".json"
  path = pre_path.format(settings.STATIC_ROOT)
  with open(path, 'r') as jsondata:
    data = json.load(jsondata)
    for k in range(0,len(data)):
      form = Sales()
      form.date = data[k]['date']
      form.amount = data[k]['amount']
      form.payed = data[k]['payed']
      form.pay_date = data[k]['pay_date']
      form.note = data[k]['note']
      form.customer_id = data[k]['customer_id']
      form.user_id = data[k]['user_id']
      form.save()
  q_data = Sales.objects.all()
  return render(request, 'list_sales.html', locals())

def add_sale_det(request, code_sale_det):
  #if request.method == "POST":
  pre_path_sale = "{0}/jsons/sale"+code_sale_det+".json"
  pre_path_sale_det = "{0}/jsons/detailsales3.json"
  path_sale = pre_path_sale.format(settings.STATIC_ROOT)
  path_sale_det = pre_path_sale_det.format(settings.STATIC_ROOT)
  with open(path_sale, 'r') as jsondata:
    data = json.load(jsondata)
    for k in range(0,len(data)):
      form = Sales()
      form.date = data[k]['date']
      form.amount = data[k]['amount']
      form.payed = data[k]['payed']
      form.pay_date = data[k]['pay_date']
      form.note = data[k]['note']
      form.customer_id = data[k]['customer_id']
      form.user_id = data[k]['user_id']
      form.save()
  l_sale = Sales.objects.all().last()
  cod_l_sale = l_sale.id
  path_sale_det = pre_path_sale_det.format(settings.STATIC_ROOT)
  with open(path_sale_det, 'r') as jsondata:
    data_det = json.load(jsondata)
    for i in range(0,len(data_det)):
      if data_det[i]['sale_id'] == cod_l_sale:
        form_det = SalesDetail()
        form_det.price = data_det[i]['price']
        form_det.note = data_det[i]['note']
        form_det.item_id = data_det[i]['item_id']
        form_det.place_id = data_det[i]['place_id']
        form_det.sale_id = data_det[i]['sale_id']
        form_det.qty = data_det[i]['qty']
        form_det.save()
  q_data_det = SalesDetail.objects.filter(sale_id = cod_l_sale)
  return render(request, 'list_sale_det.html', locals())

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