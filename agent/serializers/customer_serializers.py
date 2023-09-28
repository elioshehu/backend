from django.contrib.auth.models import User, Group
from rest_framework import serializers

from agent.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'company_name', 'deleted']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model =
        fields = ['user_id', 'group_id']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
