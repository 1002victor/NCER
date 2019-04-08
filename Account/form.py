# -*- coding: utf-8 -*-
from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password1 = forms.CharField(label='设置密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    validcode = forms.CharField(label='验证码', max_length=4)
    email = forms.EmailField(label="电子邮件")


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密  码', widget=forms.PasswordInput())