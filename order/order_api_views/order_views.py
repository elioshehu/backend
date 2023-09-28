from rest_framework.generics import ListCreateAPIView

from order.models import Order, OrderUnit, Counter
from order.serializers.order_serializers import OrderSerializer, OrderUnitSerializer, CounterSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUnitListCreateAPIView(ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer


class CounterListCreateAPIView(ListCreateAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
