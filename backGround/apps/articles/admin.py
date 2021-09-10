import xadmin
from .models import *

# Register your models here.


class ArticleAdmin:
    list_display = ['name', 'content',  'author', 'click_num', 'fav_num', 'is_hot', 'typ']
    search_fields = ['name', 'author']
    list_editable = ['is_hot']
    list_filter = ['author', 'typ']
    style_fields = {"content": "TextField"}

    class ArticlesImagesInline:
        model = ArticleImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [ArticlesImagesInline]


xadmin.site.register(Article, ArticleAdmin)
