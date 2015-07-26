from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Sucursal

class SinginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class SucursalForm(ModelForm):
	class Meta:
		model = Sucursal
		fields = ('name',)