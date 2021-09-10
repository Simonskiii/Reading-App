from __future__ import absolute_import
import os

import django
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backGround.settings')

django.setup()
app = Celery('background')

app.config_from_object('django.conf:settings')  #制定celery配置文件
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  #任务
app.conf.result_backend = "redis://localhost:6379/0" #结果保持

