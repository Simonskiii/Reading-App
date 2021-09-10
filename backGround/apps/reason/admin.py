import xadmin
from .models import *


class ReasonAdmin:
    list_display = ['content', 'typ']
    search_fields = ['typ', ]
    list_editable = ['content', 'typ']
    list_filter = ['typ']
    style_fields = {"content": "TextField"}


xadmin.site.register(Reason,ReasonAdmin)
