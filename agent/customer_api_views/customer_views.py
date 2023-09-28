from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView

from agent.models import Customer
from agent.serializers.customer_serializers import CustomerSerializer, UserSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.first()
        return User.objects.all()

# class UserGroupsListCreateAPIView(ListCreateAPIView):
#     queryset = .objects.all()
#     serializer_class = UserGroupsSerializer
