from .models import *
from rest_framework import serializers

class SalesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sales
		fields = ('user', 'amount','date', 'payed', 'pay_date', 'customer')

class SalesDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesDetail
		fields = ('sale', 'item', 'qty', 'price', 'place')
