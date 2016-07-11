import autocomplete_light
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Unit
from .models import Stock

class UnitForm(ModelForm):
	class Meta:
		model = Unit
		fields = ('unit',)

class StockForm(ModelForm):
    class Meta:
        model = Stock
        autocomplete_fields = ("description",)
        fields = ('brand', 'qty', 'description', 'code', 'date_end', 'price_base', 'units', 'place', 'note', 'parts')
        widgets = {
           "description":autocomplete_light.TextWidget("StockDescAutocomplete"),
        }