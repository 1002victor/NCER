import xadmin
from xadmin import views
from .models import *

# Register your models here.


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = '计算机等级刷题系统'
    # 设置base_site.html的Footer
    site_footer = '2018 |沪ICP备17057344号'


xadmin.site.register(views.CommAdminView, GlobalSetting)


class RolesAdmin(object):
    list_display = ('name', 'code','privilege','Disabled')
    list_editable = ('code','privilege','Disabled')
    model_icon = 'fa fa-users'


xadmin.site.register(Roles,RolesAdmin)


class LevelAdmin(object):
    list_display = ('name', 'start','end')
    list_editable = ('start','end')
    model_icon = 'fa fa-star'


xadmin.site.register(Level,LevelAdmin)


class MenuAdmin(object):
    list_display = ('Name', 'Url','Code', 'Icon', 'Index', 'Parent', 'IsPublish', 'Status')
    list_editable = ('Code', 'Url','Icon', 'Index', 'Parent', 'IsPublish', 'Status')
    model_icon = 'fa fa-sitemap'

xadmin.site.register(Menu, MenuAdmin)