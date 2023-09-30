from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from agent.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'company_name', 'deleted']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'username', 'password']


# class UserGroupsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User.groups
#         fields = ['user_id', 'group_id']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class MyTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token
