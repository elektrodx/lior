from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UnitForm

def add_unit(request):
	if request.method == "POST":
		form = UnitForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_unit')
	else:
		form = UnitForm()
	return render(request, 'add_unit.html', {'form': form })
