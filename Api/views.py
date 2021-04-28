from django.shortcuts import render
from .models import Menu, Cart
from .seralizer import MenuSerializer
from django.http import JsonResponse,request
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    if request.method == "GET":
        a = Menu.objects.all()
    elif request.method == "POST":
        a = Menu.objects.create(item_name=request.item_name, price=request.price)
        a.save()
    return render(request, "index.html", {"a": a})


def menu_list(request):
    if request.method == "GET":
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "post":
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)



def cart_list(request):
    if request.method == "GET":
        cart = Cart.objects.all()
        serializer = MenuSerializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "post":
        data = JSONParser().parse(request)

        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)

