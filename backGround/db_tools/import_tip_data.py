import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")

import django
django.setup()

from tip.models import Tip

from db_tools.data.tip_data import row_data

for tip_detail in row_data:
    tip = Tip()
    tip.typ = tip_detail["type"]
    tip.content = tip_detail["content"]
    tip.save()
