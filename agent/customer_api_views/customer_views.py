from django.contrib.auth.models import User, Group
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from agent.models import Customer
from agent.serializers.customer_serializers import CustomerSerializer, UserSerializer, GroupSerializer, \
    MyTokenObtainPairSerializer, UserReadSerializer, ShitesSerializer, ShitesUpdateSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # lookup_field = 'id'


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().prefetch_related('groups')
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserReadSerializer
        else:
            return self.serializer_class


# class GroupListCreateAPIView(ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# class GroupListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     lookup_field = 'id'


# class UserGroupsListCreateAPIView(ListCreateAPIView):
#     queryset = User.groups.all()
#     serializer_class = UserGroupsSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ShitesListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(groups__name__in=['Shites'])
    serializer_class = ShitesSerializer


class ShitesUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(groups__name__in=['Shites'])
    serializer_class = ShitesUpdateSerializer
    lookup_field = 'id'
