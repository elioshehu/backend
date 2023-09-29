from django.urls import path

from product.product_api_views.product_views import ProductListCreateAPIView, CategoryListCreateAPIView, \
    ProductListUpdateDestroyAPIView, CategoryListUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('productsUpdate/<int:id>', ProductListUpdateDestroyAPIView.as_view(), name='productsUD'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    path('categoriesUpdate/<int:id>', CategoryListUpdateDestroyAPIView.as_view(), name='categoriesUD'),
]
