# Generated by Django 2.2.4 on 2019-11-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', help_text='Reason内容', max_length=100, null=True, verbose_name='Reason内容')),
                ('typ', models.CharField(choices=[('sqz', '湿气重'), ('poor_sleep', '睡眠质量差'), ('low_dkl', '抵抗力低下'), ('little_hair', '脱发')], default='little_hair', max_length=20, verbose_name='种类')),
            ],
            options={
                'verbose_name': '病因',
                'verbose_name_plural': '病因',
            },
        ),
    ]