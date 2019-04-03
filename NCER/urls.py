# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('66/', views.python_66),
    path('24/', views.c_24),
    path('39/', views.embeded_39),
    path('45/', views.embeded_45),
]