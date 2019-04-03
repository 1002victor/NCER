# -*- coding: utf-8 -*-
from django.shortcuts import render
from Account.menu import GetAvailableRootMenu
from django.conf import settings
import random
from django.http import HttpResponse

# Create your views here.


def global_setting(request):
    ctx=dict()
    ctx["ICP"] = settings.SITE_ICP
    ctx["menus"] = GetAvailableRootMenu()
    if request.user.is_authenticated:
        ctx["username"] = request.user.username
        ctx["islogin"] = True
    else:
        ctx["username"] = "小破孩"
        ctx["islogin"] = False
    return ctx


def index(request):
    ctx=dict()
    ctx['pagetitle'] = '首页-计算机等级考试刷题系统'
    return render(request, "index.html", ctx)