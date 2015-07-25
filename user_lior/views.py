# coding=utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from .forms import SinginForm

def singin(request):
	form = SinginForm(request.POST)
	error_m = ''
	if request.method == 'POST':
		if form.is_valid:
			user_f = request.POST['username']
			pass_f = request.POST['password']
			access = authenticate(username=user_f, password=pass_f)
			if access is not None:
				if access.is_active:
					login(request, access)
					return HttpResponseRedirect('/')
				else:
					error_m = "el usuario no esta activo"
			else:
				error_m = "el usuario o la contraseña no son correctos"		
	return render(request, 'singin.html', {"form": form, "error_m": error_m }) 
