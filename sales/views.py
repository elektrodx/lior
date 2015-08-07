from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *

def add_sale(request):
	if request.method == "POST":
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = SalesForm()
	return render(request, 'add_sale.html', {'form': form })

