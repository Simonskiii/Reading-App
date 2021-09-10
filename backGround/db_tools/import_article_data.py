import random
import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")

import django
django.setup()

from articles.models import Article

from db_tools.data.article_data import row_data

for a_detail in row_data:
    article = Article()
    article.typ = a_detail["type"]
    article.name = a_detail['name']
    article.author = a_detail['author']
    article.content = a_detail['content']
    article.click_num = random.randint(0, 200)
    article.fav_num = random.randint(0, 200)
    article.aritcle_brief = a_detail['content'][0:30]
    article.save()