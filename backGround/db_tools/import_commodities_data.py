import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")

import django
django.setup()

from goods.models import Goods

from db_tools.data.commodities import row_data

for c_detail in row_data:
    good = Goods()
    good.typ = c_detail["type"]
    good.goods_brief = c_detail["goods_brief"]
    good.goods_front_image = c_detail["image"]
    good.name = c_detail["name"]
    good.save()
