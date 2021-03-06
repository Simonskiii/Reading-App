# Generated by Django 2.2.4 on 2019-11-28 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_verifycode_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='出生年月'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=20, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='haha', max_length=30, verbose_name='姓名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='typ',
            field=models.CharField(max_length=100, verbose_name='病症'),
        ),
    ]
