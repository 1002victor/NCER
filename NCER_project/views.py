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
        ctx["usernick"] = request.user.accumulate
        ctx["useravatar"] = request.user.avatar
    else:
        ctx["username"] = "小破孩"
        ctx["usernick"] = '-游客-<a herf="/account/login" style="text-decoration:none">登陆</a>|' \
                          '<a herf="/account/register">注册</a>'
        ctx["useravatar"] = "avatar/default.png"
    return ctx


def index(request):
    ctx=dict()
    ctx['pagetitle'] = '首页-计算机等级考试刷题系统'
    return render(request, "index.html", ctx)

def search(request):
    ctx = dict()
    if request.user.is_authenticated:
        ctx['pagetitle'] = '搜索(游客-未登录)'
    else:
        ctx['pagetitle'] = '搜索'
    if request.method == "GET":
        ctx['searchinfo'] = request.GET.get('search')
        print(ctx['searchinfo'])
    return render(request, "search.html", ctx)
