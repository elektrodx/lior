from django.forms import ModelForm
from .models import *

class SalesForm(ModelForm):
	class Meta:
		model = Sales
		fields = '__all__'

class SalesDetailForm(ModelForm):
	class Meta:
		model = SalesDetail
		fields = '__all__'

		