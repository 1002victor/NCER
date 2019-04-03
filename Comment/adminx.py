# -*- coding: utf-8 -*-

# from django.contrib import admin
import xadmin
from Comment.models import *

class CommentsAdmin(object):

    list_display = ('Question','Comment', 'ThumbUps', 'Disabled', 'Remark')
    list_editable = ('Disabled', 'Remark')
    model_icon = 'fa fa-comments'


xadmin.site.register(Comments, CommentsAdmin)
