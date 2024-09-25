from rest_framework import serializers
from .models import Drug, Order

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'name', 'description', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    drug_name = serializers.ReadOnlyField(source='drug.name')

    class Meta:
        model = Order
        fields = ['id', 'drug', 'drug_name', 'quantity', 'date_ordered']
