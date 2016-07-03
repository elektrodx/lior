from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
import os, json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SalesSerializer, SalesDetailSerializer

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
def sales_postjson(request):
  if request.method == 'POST':
    if request.is_ajax():
      data = request.body
      return data
    s = Sales()
    s.amount = data.amount
    s.save()
    return render(request,'home.html')


class SalesViewSet(viewsets.ModelViewSet):
  queryset = Sales.objects.all()
  serializer_class = SalesSerializer

class SalesDetailViewSet(viewsets.ModelViewSet):
  queryset = SalesDetail.objects.all()
  serializer_class = SalesDetailSerializer

@api_view(['GET', 'POST'])
def sale_list(request, format=None):
    if request.method == 'POST':
        serializer = SalesSerializer(data=request.data)
        print serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
