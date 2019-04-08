# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.do_login),
    path('logout/', views.do_logout),
    path('userinfo/', views.userinfo),
    path('get_validcode_img/', views.get_validcode_img),
]