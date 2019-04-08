# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .form import UserRegisterForm, LoginForm
from .models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from django.conf import settings
import os

from Common_Whell import validcode
# Create your views here.


def index(request):
    return HttpResponse("Hello world ! ")


def register(request):
    ctx = dict()
    ctx['pagetitle'] = '用户注册'
    if request.method == "POST":
        print(request)
        urf = UserRegisterForm(request.POST)
        if urf.is_valid():
            username = urf.cleaned_data['username']
            password1 = urf.cleaned_data['password1']
            password2 = urf.cleaned_data['password2']
            validcode = urf.cleaned_data['validcode']
            email = urf.cleaned_data['email']
            session_validcode = request.session.get('validcode')
            ctx['urf'] = urf
            if validcode.upper() == session_validcode.upper():
                if password1 != password2:
                    ctx['error'] = "请重新确认密码，两次密码不相同"
                    return render(request, 'register.html', ctx)
                user_list = User.objects.filter(username=username)
                if user_list:
                    ctx['error'] = "用户名已存在"
                    return render(request, 'register.html', ctx)
                else:
                    user = User()
                    user.username = username
                    user.password = make_password(password1)
                    user.email = email
                    user.save()
                    uf = LoginForm()
                    return HttpResponseRedirect('/account/login')
            else:
                ctx['error'] = "验证码错误"
                return render(request, 'register.html', ctx)
    else:
        urf = UserRegisterForm()
        ctx['urf'] = urf
        return render(request, 'register.html', ctx)


def do_login(request):
    ctx = dict()
    ctx['pagetitle'] = '用户登陆'
    if request.method == "POST":
        lf = LoginForm(request.POST)
        ctx['lf'] = lf
        if lf.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            print(username+password)
            if username == "" or password == "":
                ctx['error'] = "用户名和密码不能为空"
                return render(request, 'login.html', ctx)
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    ctx['error'] = "用户名和密码错误"
                    return render(request, "login.html", ctx)
    else:
        lf = LoginForm()
        ctx['lf'] = lf
        return render(request, 'login.html', ctx)


def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return HttpResponseRedirect("/")


@login_required
def userinfo(request):
    return HttpResponse("Hello world ! ")


def get_validcode_img(request):
    font_path = os.path.join(settings.BASE_DIR, "statics", "fonts", "Arial.ttf")
    print(font_path)
    valid_list = validcode.generate_validcode()
    valid_str = "".join(valid_list)
    # 把验证码保存在session中，当用户出入验证码发送请求的时候，把用户输入的数据和session中的验证码做对比
    request.session["validcode"] = valid_str
    data = validcode.make_validcode_img(valid_list, font_path)
    return HttpResponse(data, content_type='image/png')
