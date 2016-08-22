import autocomplete_light
from django.forms import ModelForm
from .models import Expenses

class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        autocomplete_fields = ("concept",)
        fields = ('provider','amount','concept','note',)
        widgets = {
        "concept":autocomplete_light.TextWidget("ExpensesDescAutocomplete"),
        }

