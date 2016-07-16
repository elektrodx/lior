from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Providers
from .models import Customers
from django.forms import widgets

class ProvidersForm(ModelForm):
	class Meta:
		model = Providers
		fields = ('name', 'email', 'address', 'fono', 'account', 'bank_account', 'contact')

class CustomersForm(ModelForm):
	class Meta:
		model = Customers
		fields = '__all__'