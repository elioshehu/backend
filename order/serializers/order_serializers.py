from rest_framework import serializers

from order.models import Order, Counter, OrderUnit


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['id', 'name', 'value']


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['product', 'amount']


class OrderUnitReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['order', 'product', 'amount', 'price']


class OrderReadSerializer(serializers.ModelSerializer):
    units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'creator', 'date_registered', 'units']


class OrderSerializer(serializers.ModelSerializer):
    units = OrderUnitSerializer(many=False)
    counter = CounterSerializer(many=False)

    class Meta:
        model = Order
        fields = ['customer', 'creator', 'units']

    def create(self, validated_data):
        units_data = validated_data.pop('units')
        order = Order.objects.create(**validated_data)
        OrderUnit.objects.create(order=order, **units_data)
        counter_data = validated_data.pop('counter')
        if counter_data.value is None:

        return order


class OrderUpdateSerializer(serializers.ModelSerializer):
    units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'creator', 'units']

        def update(self, instance, validated_data):
            data = validated_data.copy()
            units = data.pop('units', [])
            for key, val in data.items():
                setattr(instance, key, val)
            instance.save()

            unit_ids = [u['id'] for u in units]
            instance.units.clear()
            for u in unit_ids:
                instance.units.add(u)
            return instance
