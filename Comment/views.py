# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def comment(request):
    pass


def thumbup(request):
    pass


@login_required
def index(request):

    return HttpResponse("Hello world ! ")
