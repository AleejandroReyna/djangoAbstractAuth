from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta(object):
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password', 'birthday')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserCreateSerializer, self).create(validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    updated_at = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('email', 'first_name', 'last_name', 'birthday', 'updated_at', 'username')
