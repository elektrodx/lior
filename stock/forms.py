from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Unit
from .models import Stock
from django.forms import widgets

class UnitForm(ModelForm):
	class Meta:
		model = Unit
		fields = ('unit',)

class StockForm(ModelForm):
	class Meta:
		model = Stock
		fields = ('brand', 'qty', 'description', 'code', 'date_end', 'price_base', 'units', 'place', 'note')