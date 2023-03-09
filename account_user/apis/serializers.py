from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account_user.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user_details': self.user.get_basic_details()})
        return data


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password')

    def get_fields(self):
        fields = super(UserModelSerializer, self).get_fields()
        for field in fields.values():
            field.required = True
        return fields

    def create(self, validated_data):
        user = super(UserModelSerializer, self).create(validated_data)
        user.set_password(user.password)
        user.is_active = False
        user.save()
        return user

    def to_representation(self, instance):
        data = instance.get_basic_details()
        return data
