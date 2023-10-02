from django.urls import path

from order.order_api_views.order_views import OrderListCreateAPIView, OrderUnitListCreateAPIView, \
    CounterListCreateAPIView, OrderListUpdateDestroyAPIView, OrderUnitListUpdateDestroyAPIView, \
    CounterListUpdateDestroyAPIView, OrderListAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='orders'),
    path('ordersList/', OrderListAPIView.as_view(), name='ordersList'),
    path('ordersUpdate/<int:id>', OrderListUpdateDestroyAPIView.as_view(), name='ordersUD'),
    path('orderUnits/', OrderUnitListCreateAPIView.as_view(), name='orderUnits'),
    path('orderUnitsUpdate/<int:id>', OrderUnitListUpdateDestroyAPIView.as_view(), name='orderUnitsUD'),
    path('counters/', CounterListCreateAPIView.as_view(), name='counters'),
    path('countersUpdate/<int:id>', CounterListUpdateDestroyAPIView.as_view(), name='countersUD'),
]