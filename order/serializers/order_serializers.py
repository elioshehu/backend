from rest_framework import serializers

from order.models import Order, Counter, OrderUnit


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['code', 'code_year', 'date_registered', 'customer', 'creator']


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['order', 'product', 'amount', 'price']


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['name', 'value']
