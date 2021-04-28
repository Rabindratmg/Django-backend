from rest_framework import serializers
from .models import Menu,Cart


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "item_name", "price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "item_name", "price"]