from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Providers
from django.forms import widgets

class ProvidersForm(ModelForm):
	class Meta:
		model = Providers
		fields = ('name', 'email', 'address', 'fono', 'account', 'bank_account', 'contact')
		
		
