from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="userlogin"),
    path('logout/', userLogout, name="userlogout"),
    path('sifre_degistir/', sifreDegistir, name="sifre_degistir"),
    path('user_delete/', user_delete, name="user_delete")
]