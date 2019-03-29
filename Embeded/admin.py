from django.contrib import admin
from Embeded.models import *
# Register your models here.


class OptionInline(admin.TabularInline):
    model = Options


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('Question', 'Option', 'IsAnswer')
    list_editable = ('Option', 'IsAnswer')


admin.site.register(Options, OptionsAdmin)


class ChoiceQuestionsAdmin(admin.ModelAdmin):
    #list_editable = ('Level', 'Type'),
    search_fields = ('Desc',)
    inlines = [OptionInline]  # Inline
    OptionInline.min_num = 4
    OptionInline.max_num = 6
    fieldsets = (
        ['Main', {
            'fields': ('Desc', 'Level','Type','Answer'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('Difficulty','Disabled', 'Remark'),
        }]
    )


admin.site.register(ChoiceQuestions, ChoiceQuestionsAdmin)
