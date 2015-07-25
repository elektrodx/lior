from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProvidersForm

def add_provider(request):
	if request.method == "POST":
		form = ProvidersForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ProvidersForm()
	return render(request, 'add_provider.html', {'form': form })
