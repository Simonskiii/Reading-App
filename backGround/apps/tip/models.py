from django.db import models


# 解决方案
class Tip(models.Model):
    content = models.CharField(default='', max_length=100, verbose_name='tip内容', help_text='tip内容', null=True)
    typ = models.CharField(max_length=20, choices=(('sqz', u'湿气重'), ('poor_sleep', u'睡眠质量差'), ('low_dkl', u'抵抗力低下'),
                                                   ('little_hair', u'脱发')), default="little_hair",
                           verbose_name="种类")

    class Meta:
        verbose_name = '小知识'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

