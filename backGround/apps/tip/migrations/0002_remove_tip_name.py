# Generated by Django 2.2.4 on 2019-11-24 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='name',
        ),
    ]
