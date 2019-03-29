# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from Python.models import *
import random


def index(request):
    ctx = dict()
    rand_item = random.choice(ChoiceQuestions.objects.all())
    item_options = Options.objects.filter(Question_id=rand_item.id)
    ctx["timu"] = rand_item
    ctx["xuanxiang"] = item_options
    return render(request, '2_python/py_choice.html', ctx)


def index2(request):
    ctx = dict()
    rand_item = random.choice(ProgramingQuestions.objects.all())
    ctx["timu"] = rand_item
    return render(request, '2_python/py_programing.html', ctx)