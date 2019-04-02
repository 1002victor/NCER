from django.db import models

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