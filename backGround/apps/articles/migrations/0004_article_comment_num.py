# Generated by Django 2.2.4 on 2019-11-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191129_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_num',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
    ]