from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/singin")
def add_shop(request):
	if request.method == "POST":
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ShopForm()
	return render(request, 'add_shop.html', {'form': form })
