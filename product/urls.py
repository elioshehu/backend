from django.urls import path

from product.product_api_views.product_views import ProductListCreateAPIView, CategoryListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
]
