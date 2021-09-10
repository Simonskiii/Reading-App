from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.utils import timezone


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="姓名")
    birthday = models.DateField(null=False, blank=False, verbose_name="出生年月")
    gender = models.CharField(max_length=20, choices=(("male", u"男"), ("female", "女")), default="male",
                              verbose_name="性别")
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name="邮箱", default='')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    typ = models.CharField(max_length=500, null=False, blank=False, verbose_name="病症")
    tag = models.TextField(default='', verbose_name='user标签', help_text='user标签', null=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name='用户邮箱', default='')
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")
    send_type = models.CharField(max_length=20, verbose_name='发送类型', default='')

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
