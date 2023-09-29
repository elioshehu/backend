from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from order.models import Order, OrderUnit, Counter
from order.serializers.order_serializers import OrderSerializer, OrderUnitSerializer, CounterSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'


class OrderUnitListCreateAPIView(ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer


class OrderUnitListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer
    lookup_field = 'id'


class CounterListCreateAPIView(ListCreateAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    lookup_field = 'id'
