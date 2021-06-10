
from django.shortcuts import render
from .models import Menu, Cart
from .seralizer import MenuSerializer,CartSerializer, UserSerializer
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.




def home(request):
    if request.method == "GET":
        a = Menu.objects.all()
    elif request.method == "POST":
        a = Menu.objects.create(item_name=request.POST.get('item'), price=request.POST.get('price'))
        a.save()
        a=Menu.objects.all()
    return render(request, "index.html", {"a": a})
    

class MenuList(viewsets.ModelViewSet):
    queryset= Menu.objects.all()
    serializer_class = MenuSerializer

class CartList(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer 


class UserList(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes =[IsAuthenticated]
    queryset= User.objects.all()
    serializer_class = UserSerializer