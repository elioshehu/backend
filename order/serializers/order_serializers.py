from rest_framework import serializers

from order.models import Order, Counter, OrderUnit

from product.serializers.product_serializer import ProductReadSerializer


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['id', 'name', 'value']


class OrderUnitSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    price = serializers.IntegerField(required=False)
    name = serializers.SerializerMethodField('get_name')

    class Meta:
        model = OrderUnit
        fields = ['id', 'product', 'amount', 'price', 'name']

    def get_name(self, obj):
        return obj.product.name
    # def create(self, validated_data):
    #     if not validated_data['price']:
    #         product = Product.objects.get(pk=validated_data['product'])
    #         validated_data['price'] = product.default_price
    #     return OrderUnit.objects.create(**validated_data)


class OrderUnitReadSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    class Meta:
        model = OrderUnit
        fields = ['id', 'product', 'amount', 'price', 'name']

    def get_name(self, obj):
        return obj.product.name


class OrderReadSerializer(serializers.ModelSerializer):
    units = OrderUnitSerializer(many=True)
    customer = serializers.SerializerMethodField('get_customer_name')
    creator = serializers.SerializerMethodField('get_creator_name')

    # products_name = ProductReadSerializer(source='units', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'creator', 'date_registered', 'units']

    def get_customer_name(self, obj):
        return obj.customer.first_name

    def get_creator_name(self, obj):
        return obj.creator.username


class OrderSerializer(serializers.ModelSerializer):
    units = OrderUnitSerializer(many=True)

    # products_name = ProductReadSerializer(source='units', many=True, read_only=True)
    # counter = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'creator', 'units']

    def update(self, instance, validated_data):
        data = validated_data.copy()
        units = data.pop('units')
        # instance.creator = validated_data.get('creator')
        for key, val in data.items():
            setattr(instance, key, val)
        instance.save()
        instance.units.all().delete()
        for unit in units:
            # if unit.get('id', 0) > 0:
            #     new_unit = OrderUnit.objects.get(id=unit['id'])
            #     new_unit.product = unit['product']
            #     new_unit.amount = unit['amount']
            #     new_unit.save()
            # else:
            # unit['id'] = 0
            # unit.pop('id')
            OrderUnit.objects.create(order=instance, **unit)
        return instance

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
            # unit_to_add = unit.pop('id')
            if unit.get('price', 0) == 0:
                product = unit['product']
                unit['price'] = product.default_price
            OrderUnit.objects.create(**unit, order_id=order.pk)
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
