# -*- coding: utf-8 -*-
from .models import Menu


def GetAvailableRootMenu():
    return Menu.objects.filter(Status="A", Parent="root", IsPublish=True)
