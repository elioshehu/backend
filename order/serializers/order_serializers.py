from rest_framework import serializers

from order.models import Order, Counter, OrderUnit


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['id', 'name', 'value']


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['id', 'product', 'amount']


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
    # units = OrderUnitSerializer(many=True)
    # counter = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Order
        fields = ['customer', 'creator', 'units']

    # def update(self, instance, validated_data):
    #     print('Running order')
    #     data = validated_data.copy()
    #     units = data.pop('units', [])
    #     for key, val in data.items():
    #         setattr(instance, key, val)
    #     instance.save()
    #
    #     print(units)
    #     print(units[0])
    #
    #     unit_ids = [u['id'] for u in units]
    #     print(unit_ids)
    #     instance.units.clear()
    #     for u in unit_ids:
    #         instance.units.add(u)
    #     return instance

    def create(self, validated_data):
        units_data = validated_data.pop('units')
        if Counter.objects.first() is None:
            Counter.objects.create(name='Order', value=1)
        counter = Counter.objects.first()
        order_check = Order.objects.last()
        order = Order.objects.create(**validated_data)
        if order_check.code_year != order.code_year:
            counter.value = 1
        order.code = f'P-{counter.value}-{order.code_year}'
        order.save()
        counter.value += 1
        counter.save()
        for unit in units_data:
            OrderUnit.objects.create(order=order, **unit)
        return order

    # def set_code(self, counter):

# class OrderUpdateSerializer(serializers.ModelSerializer):
#     # units = OrderUnitSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = ['customer', 'creator', 'units']
#
#
