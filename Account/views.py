# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .form import UserRegisterForm, LoginForm
from .models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf

# Create your views here.


def index(request):
    return HttpResponse("Hello world ! ")


def register(request):
    if request.method == "POST":
        print(request)
        urf = UserRegisterForm(request.POST)
        if urf.is_valid():
            username = (request.POST.get('username')).strip()
            password1 = (request.POST.get('password')).strip()
            password2 = (request.POST.get('password')).strip()
            email = (request.POST.get('email')).strip()
            if password1 != password2:
                return render(request, 'register.html', {'urf': urf, 'error': "请重新确认密码，两次密码不相同"})
            user_list = User.objects.filter(username=username)
            if user_list:
                return render(request,'register.html', {'urf': urf, 'error': "用户名已存在"})
            else:
                user=User()
                user.username = username
                user.password = make_password(password1)
                user.email = email
                user.save()
                uf = LoginForm()
                return HttpResponseRedirect('/account/login')
    else:
        urf = UserRegisterForm()
        return render(request,'register.html', {'urf': urf})


def do_login(request):
    if request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            print(username+password)
            if username == "" or password == "":
                return render(request, 'login.html', {'lf': lf, 'error': "用户名和密码不能为空"})
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return render(request, "login.html", {'lf': lf, 'error': "用户名和密码错误"})
    else:
        lf = LoginForm()
        return render(request, 'login.html', {'lf': lf})


def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return HttpResponseRedirect("/")


@login_required
def userinfo(request):
    return HttpResponse("Hello world ! ")

