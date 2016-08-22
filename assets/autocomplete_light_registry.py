import autocomplete_light
from .models import Expenses

class ExpensesDescAutocomplete(autocomplete_light.AutocompleteModelBase):
	# Para incluir mas campos de busqueda
    search_fields = ['^concept',]
    attrs = {'placeholder': 'Concepto del Gasto', 'data-autocomplete-minimum-characters': 1,}

autocomplete_light.register(Expenses, ExpensesDescAutocomplete)
