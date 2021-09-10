import xadmin
from .models import *


class UserReadAricleAdmin:
    list_display = ['user', 'article', 'articleName', 'time']
    search_fields = ['typ', 'userName', 'articleName']
    list_filter = ['articleName', ]


class UserFavAricleAdmin:
    list_display = ['user', 'article', 'articleName', 'time']
    search_fields = ['typ', 'userName', 'articleName']
    list_filter = ['articleName', ]

class CommentAdmin:
    list_display = ['content', 'time', 'userName', 'articleName']
    search_fields = ['typ', 'userName', 'articleName']
    list_filter = ['articleName', 'userName']


xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(UserReadAricle, UserReadAricleAdmin)
xadmin.site.register(UserFavAricle, UserFavAricleAdmin)
