from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('menu',views.MenuList, basename='menulist')
router.register('user',views.UserList, basename='userlist')
router.register('cart',views.CartList, basename='cartlist')


urlpatterns = [
    path("", views.home, name="home"),
    path("api/",include(router.urls), name="menulist"),
]