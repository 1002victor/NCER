from django.db import models

# Create your models here.


class Type(models.Model):
    Name = models.CharField(max_length=30,verbose_name="题目类型")
    Desc = models.CharField(max_length=30, verbose_name="类型说明")
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '主类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class SubType(models.Model):
    Name = models.CharField(max_length=30, verbose_name="题目类型")
    Desc = models.CharField(max_length=30, verbose_name="类型说明")
    MainType = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="类型")
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '题目类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class Levels(models.Model):
    Name = models.CharField(max_length=30,verbose_name="考试分类")
    Code = models.IntegerField(default=00, verbose_name="科目代码")
    Desc = models.CharField(max_length=30, verbose_name="类型说明")
    Disabled = models.BooleanField(default=False, verbose_name="删除")
    CreateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    CreateBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="创建人")
    ModifyTime = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")
    ModifyBy = models.CharField(max_length=50, null=True, blank=True, verbose_name="修改人")
    Remark = models.CharField(max_length=1000, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '考试等级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name
