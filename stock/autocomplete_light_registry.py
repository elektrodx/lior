import autocomplete_light
from .models import Stock

class StockDescAutocomplete(autocomplete_light.AutocompleteModelBase):
	# Para incluir mas campos de busqueda
    search_fields = ['^code','^description',]
    attrs = {'placeholder': 'Codigo o Nombre Producto', 'data-autocomplete-minimum-characters': 1,}

autocomplete_light.register(Stock, StockDescAutocomplete)
