from django.urls import path

from order.order_api_views.order_views import OrderListCreateAPIView, OrderUnitListCreateAPIView, \
    CounterListCreateAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='orders'),
    path('orderUnits/', OrderUnitListCreateAPIView.as_view(), name='orderUnits'),
    path('counters/', CounterListCreateAPIView.as_view(), name='counters'),
]