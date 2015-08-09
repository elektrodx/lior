import autocomplete_light
from .models import Stock

class StockAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^brand',]
    attrs = {'placeholder': 'Nombre Producto', 'data-autocomplete-minimum-characters': 1,}

autocomplete_light.register(Stock, StockAutocomplete)
