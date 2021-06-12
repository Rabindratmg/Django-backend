from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu,Cart
from rest_framework.authtoken.views import Token


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "item_name", "price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

    def create(self,validated_data):
        user= User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user