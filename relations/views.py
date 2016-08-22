from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProvidersForm
from .forms import CustomersForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url="/singin")
def add_provider(request):
	if request.method == "POST":
		form = ProvidersForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ProvidersForm()
	return render(request, 'add_provider.html', {'form': form })

@login_required(login_url="/singin")
def add_provider_2(request):
  if request.method == "POST":
    form = ProvidersForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('<script type="text/javascript">window.opener.reloadMyDivProvider(); window.close();</script>')
  else:
    form = ProvidersForm()
  return render(request, 'add_provider_2.html', {'form': form })

@login_required(login_url="/singin")
def add_customer(request):
  if request.method == "POST":
    form = CustomersForm(request.POST)
    if form.is_valid():
      form.save()
      #return HttpResponseRedirect('/add_sale')
      return HttpResponse('<script type="text/javascript">window.opener.location.reload(); window.close();</script>')
  else:
    form = CustomersForm()
  return render(request, 'add_customer.html', {'form': form })

@login_required(login_url="/singin")
def add_customer_2(request):
  if request.method == "POST":
    form = CustomersForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_customer_2')
  else:
    form = CustomersForm()
  return render(request, 'add_customer_2.html', {'form': form })