from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import ListField
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from agent.models import Customer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserReadSerializer(serializers.ModelSerializer):
    # my_groups = serializers.SerializerMethodField(read_only=False)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'username', 'password', 'groups']


class UserSerializer(serializers.ModelSerializer):
    # my_groups = serializers.SerializerMethodField(read_only=False)
    groups_name = GroupSerializer(source='groups', many=True, read_only=True)

    # groups = serializers.ListSerializer(child=serializers.IntegerField())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'username', 'password', 'groups', 'groups_name']

        # def update(self, instance, validated_data):
        #     data = validated_data.copy()
        #     groups = data.pop('groups', [])
        #     for key, val in data.items():
        #         setattr(instance, key, val)
        #     instance.save()
        #
        #     group_ids = [g['id'] for g in groups]
        #     instance.groups.clear()
        #     for g in group_ids:
        #         instance.groups.add(g)
        #     return instance

        # def create(self, validated_data):
        #     data = validated_data.copy()
        #     groups = validated_data.pop('groups', [])
        #     instance = self.Meta.model.objects.create(**data)
        #     for group in groups:
        #         instance.groups.add(group)
        #     return instance

    # def to_representation(self, instance):
    #     data = super(UserSerializer, self).to_representation(instance)
    #     groups = instance.groups.all()
    #     arr = []
    #     for g in groups:
    #         arr.append({'name': g.name, 'id': g.id})
    #     data['groups'] = arr
    #     return data


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'company_name']


# class UserGroupsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User.groups
#         fields = ['user_id', 'group_id']


class ShitesSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    groups_name = GroupSerializer(source='groups', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'groups_name']

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        g = Group.objects.get(name='Shites')
        instance.groups.add(g)
        return instance


class ShitesUpdateSerializer(serializers.ModelSerializer):
    groups_name = GroupSerializer(source='groups', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'groups_name']


class MyTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        token = self.get_token(self.user)
        data['access'] = str(token.access_token)
        data['refreshToken'] = str(token)
        data['username'] = self.user.username
        data['id'] = self.user.id
        return data
