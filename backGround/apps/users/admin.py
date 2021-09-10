import xadmin
from .models import *
from xadmin import views
# Register your models here.


class GlobalSettings:
    """
    后台修改
    """
    site_title = '课设后台管理系统'
    site_footer = '课设后台管理系统'
      # 开启分组折叠


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class UserProfileAdmin:
    """
    用户
    """
    list_display = ['name', 'birthday', 'gender', 'email', 'image', 'typ', 'tag']
    search_fields = ['name', 'email']
    list_filter = ['name', 'email']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
