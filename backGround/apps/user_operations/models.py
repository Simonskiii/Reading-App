from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from articles.models import Article, ArticleCatergory

User = get_user_model()


# Create your models here.

# 阅读记录
class UserReadAricle(models.Model):
    user = models.ForeignKey(User, verbose_name="用户名", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='文章题目', on_delete=models.CASCADE)
    articleName = models.CharField(default='', max_length=50, verbose_name='题目', help_text='题目', null=True)
    time = models.DateTimeField(default=timezone.now, verbose_name="浏览时间", null=True)

    class Meta:
        verbose_name = '阅读记录'
        verbose_name_plural = verbose_name


# 收藏记录
class UserFavAricle(models.Model):
    user = models.ForeignKey(User, verbose_name="用户名", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='文章题目', on_delete=models.CASCADE)
    articleName = models.CharField(default='', max_length=50, verbose_name='题目', help_text='题目', null=True)
    time = models.DateTimeField(default=timezone.now, verbose_name="收藏时间", null=True)

    class Meta:
        verbose_name = '收藏记录'
        verbose_name_plural = verbose_name


# 评论
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="用户名", on_delete=models.CASCADE)
    userName = models.CharField(max_length=30, null=False, blank=False, verbose_name="用户昵称")
    article = models.ForeignKey(Article, verbose_name='文章题目', on_delete=models.CASCADE)
    content = models.TextField(default="", verbose_name="评论内容", help_text="评论内容")
    articleName = models.CharField(default='', max_length=50, verbose_name='题目', help_text='题目', null=True)
    time = models.DateTimeField(default=timezone.now, verbose_name="评论时间", null=True)

    class Meta:
        verbose_name = '评论记录'
        verbose_name_plural = verbose_name
