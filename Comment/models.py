# -*- coding: utf-8 -*-
from django.db import models
from Account.models import CommonInfo
from NCER.models import ChoiceQuestions
from Account.models import User
# Create your models here.


class Comments(CommonInfo):
    Question = models.ForeignKey(ChoiceQuestions, on_delete=models.CASCADE, verbose_name="题目")
    Comment = models.TextField(verbose_name="评论内容")
    ParentID = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name="父级评论")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='用户')
    Username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    Email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    ThumbUps = models.IntegerField(default=0, verbose_name="点赞次数")

    class Meta:
        verbose_name = '留言评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Comment
