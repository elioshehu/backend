from rest_framework import serializers

from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'deleted']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'product']


# class ProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = ['product_id', 'product_id']
