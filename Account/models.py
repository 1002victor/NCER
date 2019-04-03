# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CommonInfo(models.Model):
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    FromIP = models.GenericIPAddressField(null=True, verbose_name="IP")
    FromPlatform = models.CharField(max_length=300,null=True,verbose_name="平台")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        abstract = True
        ordering = ["CreateTime"]


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    accumulate = models.IntegerField(default=0, verbose_name="积分")
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    wechat = models.CharField(max_length=100, blank=True, null=True, verbose_name='微信')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Roles(CommonInfo):
    name = models.CharField(max_length=20, default="普通",verbose_name="等级名称")
    code = models.IntegerField(default=0,verbose_name="编号")
    privilege = models.CharField(max_length=300, blank=True, null=True, verbose_name='权限')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        ordering = ['-code']

    def __unicode__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=20, default="菜鸟",verbose_name="等级名称")
    start = models.IntegerField(default=0,verbose_name="积分下限")
    end = models.IntegerField(default=0,verbose_name="积分上限")

    class Meta:
        verbose_name = '积分'
        verbose_name_plural = verbose_name
        ordering = ['-start']

    def __unicode__(self):
        return self.name


MENU_STATUS=(
    ('D', '删除'),
    ('A', '可用'),
)


class Menu(models.Model):
    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    Name = models.CharField(max_length=50, default="", verbose_name="菜单名称")
    Url = models.CharField(max_length=30,default="/",null=True, blank=True,verbose_name="地址")
    Icon = models.CharField(max_length=50, default="ace-icon-home", verbose_name="菜单图标")
    Code = models.CharField(max_length=6, default="root", unique=True, verbose_name="菜单编号")
    Index = models.IntegerField(default=0, verbose_name="排序号")
    Parent = models.CharField(max_length=6, default="root", verbose_name="父级菜单")
    IsPublish = models.BooleanField(default=False,verbose_name="是否发布")
    Status = models.CharField(max_length=2, default='A', null=True, blank=True,choices=MENU_STATUS)

    def __str__(self):
        return self.Name

