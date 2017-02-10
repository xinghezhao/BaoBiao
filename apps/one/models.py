from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserMessage(models.Model):
    center_number = models.IntegerField(default=0, verbose_name=u'中心编号')
    center_mc = models.CharField(max_length=20, default='', verbose_name=u'中心名称')
    center_pr = models.CharField(max_length=10, default='', verbose_name=u'中心联系人')
    center_mobile = models.CharField(max_length=11, default='', verbose_name=u'联系人电话')
    address = models.CharField(max_length=10, default='', verbose_name=u'联系地址')
    modify_person = models.CharField(max_length=10, default='', verbose_name=u'修改人')
    start_time = models.DateTimeField(null=True, verbose_name=u'开始时间')
    creator = models.ForeignKey(User, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户信息录入'
        verbose_name_plural = verbose_name



