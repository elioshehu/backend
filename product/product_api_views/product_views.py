from rest_framework.generics import ListCreateAPIView

from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer, CategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
