from django.urls import path

from product.product_api_views.product_views import ProductListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
]
