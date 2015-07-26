from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Unit
from django.forms import widgets

class UnitForm(ModelForm):
	class Meta:
		model = Unit
		fields = ('unit',)
