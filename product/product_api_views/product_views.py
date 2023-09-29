from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer, CategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
# class ProductCategoryListCreateAPIView(ListCreateAPIView):
#     queryset =
#     serializer_class = ProductCategorySerializer
