from django.contrib import admin
import xadmin
from .models import *
from ckeditor.fields import RichTextField
# Register your models here.


class GoodsAdmin:
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "RichTextField"}

    class GoodsImagesInline:
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]



class HotSearchAdmin:
    list_display = ["keywords", "index", "add_time"]



xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(HotSearchWords, HotSearchAdmin)