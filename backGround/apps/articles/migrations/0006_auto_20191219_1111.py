# Generated by Django 2.2.4 on 2019-12-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.TextField(default='', help_text='article标签', null=True, verbose_name='article标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='typ',
            field=models.CharField(choices=[('sqz', '湿气重'), ('poor_sleep', '睡眠质量差'), ('low_dkl', '抵抗力低下'), ('little_hair', '脱发')], default='', max_length=20, null=True, verbose_name='种类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='', help_text='article内容', null=True, verbose_name='article内容'),
        ),
    ]
