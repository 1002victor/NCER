from django.contrib import admin
from NCER.models import *

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Desc', 'Disabled', 'Remark')
    list_editable = ('Desc', 'Disabled', 'Remark')


admin.site.register(Type, TypeAdmin)


class SubTypeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'MainType', 'Desc', 'Disabled', 'Remark')
    list_editable = ('MainType', 'Desc', 'Disabled', 'Remark')


admin.site.register(SubType, SubTypeAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Disabled', 'Remark')
    list_editable = ('Disabled', 'Remark')


admin.site.register(Tag, TagAdmin)


class OptionsAdmin(admin.ModelAdmin):
    search_fields = ('Option',)
    list_display = ('Question', 'Option', 'IsAnswer')
    list_editable = ('IsAnswer',)


class OptionInline(admin.StackedInline):
    model = Options
    fields = ('Option', 'IsAnswer')
    extra = 4


admin.site.register(Options, OptionsAdmin)


class ChoiceQuestionsAdmin(admin.ModelAdmin):
    # list_editable = ('Level', 'Type'),
    search_fields = ('Desc',)
    inlines = [OptionInline]  # Inline
    OptionInline.min_num = 4
    OptionInline.max_num  = 6
    fieldsets = (
        ['Main', {
            'fields': ('Desc', 'Level', 'Type', 'Answer'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('Difficulty', 'Disabled', 'Remark'),
        }]
    )


admin.site.register(ChoiceQuestions, ChoiceQuestionsAdmin)