from django.test import TestCase

# Create your tests here.

from .forms import SimpleForm
from .models import Stock

class SimpleFormTestCase(TestCase):

    def test_valid_form(self):
        "Submit valid data."
        thing = Thing.objects.create(name='Foo', description='Bar')
        data = {
            'thing_0': thing.name,
            'thing_1': thing.pk,
        }
        form = SimpleForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        "Thing is required but missing."
        data = {
            'thing_0': 'Foo',
            'thing_1': '',
        }
        form = SimpleForm(data=data)
        self.assertFalse(form.is_valid())