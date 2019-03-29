from django.db import models
from NCER.models import SubType, Levels
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ChoiceQuestions(models.Model):
    Level = models.ForeignKey(Levels, on_delete=models.CASCADE, verbose_name="考试分类")
    Type = models.ForeignKey(SubType, on_delete=models.CASCADE, verbose_name="类型")
    Desc = RichTextUploadingField(config_name='my_config',default='', verbose_name="题目")
    Answer = RichTextUploadingField(config_name='my_config',default='', verbose_name="答案解析")
    Difficulty = models.IntegerField(default=5, verbose_name="难度")
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '选择题'
        verbose_name_plural = verbose_name

    def __str__(self):
        if len(self.Desc)>30:
            return self.Desc[:30]+'...'
        else:
            return self.Desc


class Options(models.Model):
    Question = models.ForeignKey(ChoiceQuestions, on_delete=models.CASCADE, verbose_name="题目")
    Option = RichTextField(config_name='my_config',default='', verbose_name="选项")
    IsAnswer = models.BooleanField(verbose_name="是否为选项")
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Option

