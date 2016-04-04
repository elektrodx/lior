#import autocomplete_light
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Unit
from .models import Stock
from django.forms import widgets

class UnitForm(ModelForm):
	class Meta:
		model = Unit
		fields = ('unit',)

#class StockForm(ModelForm):
class StockForm(ModelForm):
	# description = autocomplete_light.ModelChoiceField('StockDescAutocomplete')
	class Meta:
		# = autocomplete_light.get_widgets_dict(Stock)
		model = Stock
		fields = ('brand', 'qty', 'description', 'code', 'date_end', 'price_base', 'units', 'place', 'note')
		#autocomplete_fields = ['brand']
		#autocomplete_names = {'brand': 'BrandAutocomplete'}
