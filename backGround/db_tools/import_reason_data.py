import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backGround.settings")

import django
django.setup()

from reason.models import Reason

from db_tools.data.reason_data import row_data

for r_detail in row_data:
    reason = Reason()
    reason.typ = r_detail["type"]
    reason.content = r_detail["content"]
    reason.save()