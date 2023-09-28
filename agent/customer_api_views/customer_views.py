from django.contrib.auth.models import User, Group
from rest_framework.generics import ListCreateAPIView

from agent.models import Customer
from agent.serializers.customer_serializers import CustomerSerializer, UserSerializer, GroupSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.first()
        return User.objects.all()


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# class UserGroupsListCreateAPIView(ListCreateAPIView):
#     queryset = .objects.all()
#     serializer_class = UserGroupsSerializer
