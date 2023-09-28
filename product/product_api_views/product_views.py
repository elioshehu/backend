from rest_framework.generics import ListCreateAPIView

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
