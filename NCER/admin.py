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


class LevelsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Code', 'Desc', 'Disabled', 'Remark')
    list_editable = ('Desc', 'Disabled', 'Remark')


admin.site.register(Levels,LevelsAdmin)
