# _*_ coding: utf-8 _*_

# from django.contrib import admin
import xadmin
from NCER.models import *

# Register your models here.


class TypeAdmin(object):
    list_display = ('Name', 'Desc', 'Disabled', 'Remark')
    list_editable = ('Desc', 'Disabled', 'Remark')
    model_icon = 'fa fa-angle-right'


xadmin.site.register(Type, TypeAdmin)


class SubTypeAdmin(object):
    list_display = ('Level', 'Name', 'MainType', 'Desc', 'Disabled', 'Remark')
    list_editable = ('MainType', 'Desc', 'Disabled', 'Remark')
    model_icon = 'fa fa-angle-double-right'


xadmin.site.register(SubType, SubTypeAdmin)


class TagAdmin(object):
    list_display = ('Name', 'Disabled', 'Remark')
    list_editable = ('Disabled', 'Remark')
    model_icon = 'fa fa-tags'


xadmin.site.register(Tag, TagAdmin)


class OptionsAdmin(object):
    search_fields = ('Option',)
    list_display = ('Question', 'Option', 'IsAnswer')
    list_editable = ('IsAnswer',)
    model_icon = 'fa fa-outdent'


class OptionInline(object):
    model = Options
    fields = ('Option', 'IsAnswer')
    extra = 4


xadmin.site.register(Options, OptionsAdmin)


class ChoiceQuestionsAdmin(object):
    # list_editable = ('Level', 'Type'),
    search_fields = ('Desc',)
    inlines = [OptionInline]  # Inline
    OptionInline.min_num = 4
    OptionInline.max_num = 6
    fieldsets = (
        ['Main', {
            'fields': ('Desc', 'Level', 'Type', 'Answer'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('Difficulty', 'Disabled', 'Remark'),
        }]
    )
    model_icon = 'fa fa-question'


xadmin.site.register(ChoiceQuestions, ChoiceQuestionsAdmin)