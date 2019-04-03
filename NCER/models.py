# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField
from Account.models import CommonInfo
# Create your models here.

LEVEL_CHOICES = (
    ('一级',
         (
            ('14', '计算机基础及WPS Office应用'),
            ('15', '计算机基础及MS Office应用'),
            ('16', '计算机基础及Photoshop应用'),
            ('17', '网络安全素质教育'),
         )
     ),
    ('二级',
         (
            ('24', 'C语言程序设计'),
            ('26', 'VB语言程序设计'),
            ('28', 'Java语言程序设计'),
            ('29', 'Access数据库程序设计'),
            ('61', 'C++语言程序设计'),
            ('63', 'MySQL数据库程序设计'),
            ('64', 'Web程序设计'),
            ('65', 'MS Office高级应用'),
            ('66', 'Python语言程序设计'),
         )
     ),
    ('三级',
         (
            ('35', '网络技术'),
            ('36', '数据库技术'),
            ('38', '信息安全技术'),
            ('39', '嵌入式系统开发技术'),
         )
     ),
    ('四级',
         (
            ('41', '网络工程师'),
            ('42', '数据库工程师'),
            ('44', '信息安全工程师'),
            ('45', '嵌入式系统开发工程师'),
        )
     ),
)


class Type(CommonInfo):
    Name = models.CharField(max_length=30,verbose_name="题目类型")
    Desc = models.CharField(max_length=30, verbose_name="类型说明")

    class Meta:
        verbose_name = '考题类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class SubType(CommonInfo):
    MainType = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="类型")
    Level = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name="所属考试")
    Name = models.CharField(max_length=30, verbose_name="题目主类型")
    Desc = models.CharField(max_length=30, verbose_name="类型说明")

    class Meta:
        verbose_name = '题目子类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class Tag(CommonInfo):
    Name = models.CharField(max_length=30,verbose_name="题目标签")

    class Meta:
        verbose_name = '题目标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class ChoiceQuestions(CommonInfo):
    Level = models.CharField(max_length=2, choices=LEVEL_CHOICES, verbose_name="考试分类")
    Type = models.ForeignKey(SubType, on_delete=models.CASCADE, verbose_name="类型", related_name='Type')
    Desc = models.TextField(default='', verbose_name="题目")
    Answer = models.TextField(default='', verbose_name="答案解析")
    Difficulty = models.IntegerField(default=5, verbose_name="难度")
    Tags = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '选择题'
        verbose_name_plural = verbose_name

    def __str__(self):
        if len(self.Desc) > 50:
            return self.Desc[:50]+'...'
        else:
            return self.Desc


class Options(CommonInfo):
    Question = models.ForeignKey(ChoiceQuestions, on_delete=models.CASCADE, verbose_name="题目")
    Option = models.TextField(default='', verbose_name="选项")
    IsAnswer = models.BooleanField(verbose_name="是否为正确选项")

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Option

