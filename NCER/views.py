# -*- coding: utf-8 -*-
from django.shortcuts import render
from Account.menu import GetAvailableRootMenu
from django.http import HttpResponse

# Create your views here.


def index(request):
    ctx = dict()
    ctx['pagetitle'] = '考试题库'
    return render(request, "NCER/index.html", ctx)

#二级python
def python_66(request):
    return render(request, "NCER/2/index.html")

#四级嵌入式
def embeded_45(request):
    return render(request, "NCER/4/index.html")


#三级嵌入式
def embeded_39(request):
    return render(request, "NCER/3/index.html")
#二级C
def c_24(request):
    pass