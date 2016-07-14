from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from relations.models import Customers
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
import os, json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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
def sale_list(request):
    if request.is_ajax:
      user = request.user.pk
      amount = float(request.POST.get('amount'))
      # pay_date = request.POST.get('pay_date')
      customerdni = request.POST.get('customer')
      items = request.POST.dict()
      data = ast.literal_eval(items['items'])
      pdb.set_trace()
      customer = Customers.objects.get(ci=customerdni)
      sale = Sales(user_id=user, amount=amount, payed=amount, customer_id=customer.pk)
      sale.save()
      return