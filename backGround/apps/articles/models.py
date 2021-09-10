from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
import factory
from django.utils import timezone
from faker import Factory
User = get_user_model()
fake = Factory.create()
# Create your models here.


# 文章类别
class ArticleCatergory(models.Model):
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    name = models.CharField(default='', max_length=50, verbose_name='题目', help_text='题目', null=True)
    typ = models.CharField(max_length=20, null=True, choices=(('sqz', u'湿气重'), ('poor_sleep', u'睡眠质量差'),
                                                              ('low_dkl', u'抵抗力低下'), ('little_hair', u'脱发')),
                           default="",
                           verbose_name="种类")
    content = models.TextField(default='', verbose_name='article内容', help_text='article内容', null=True)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='喜欢数')
    comment_num = models.IntegerField(default=0, verbose_name='评论数')
    aritcle_brief = models.TextField(max_length=500, verbose_name="文章概述", default='')
    article_front_image = models.ImageField(upload_to="article/images/", null=True, blank=True, verbose_name="封面图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    is_anonymous = models.BooleanField(default=False, verbose_name='是否匿名')
    # author = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_DEFAULT, default='')
    author = models.CharField(max_length=20, default='', verbose_name='作者', help_text='作者')
    time = models.DateTimeField(default=timezone.now, verbose_name="发布时间", null=False)
    tag = models.TextField(default='', verbose_name='article标签', help_text='article标签', null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



# 文章图
class ArticleImage(models.Model):
    """
    商品轮播图
    """
    articles = models.ForeignKey(Article, verbose_name="文章", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '封面图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.articles.name


# import random
# class ArticleCatergoryFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = ArticleCatergory
#     name = fake.word()
#     li = []
#     for i in name.split(" "):
#         li.append(i[0])
#     code = "".join('1')
#     catergory_type = random.randint(1,3)
#
#
# class ArticleFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Article
#     author = fake.name()
#     content = fake.text()
#     name = fake.word()
#     category = factory.SubFactory(ArticleCatergoryFactory)



