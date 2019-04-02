from django.db import models
from Account.models import CommonInfo
from NCER.models import ChoiceQuestions
# Create your models here.


class Comments(CommonInfo):
    Question = models.ForeignKey(ChoiceQuestions, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=30, verbose_name="内容")
    ParentID = models.CharField(max_length=64, default="root", verbose_name="父级评论")
    ThumbUps = models.IntegerField(default=0,verbose_name="点赞次数")

    class Meta:
        verbose_name = '留言评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Comment

