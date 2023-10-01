from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS

from order.models import Order, OrderUnit, Counter
from order.serializers.order_serializers import OrderSerializer, OrderUnitSerializer, CounterSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'


class MyCustomPermission(BasePermission):
    message = 'This is a custom permission'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

class OrderUnitListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer


class OrderUnitListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [MyCustomPermission]
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
