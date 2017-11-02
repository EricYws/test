# _*_ encoding:utf-8 _*_

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSettings(object):
    enable_themes = True  # 使用主题功能
    use_bootswatch = True

class GlobalSetting(object):
    site_title = u"YWS教育平台" #设置站名
    site_footer = u"YWS在线网" #设置@copy
    # menu_style='accordion' #设置菜单缩放

class EmailVerifyRecordAdmin(object):
    # list_dispaly表示要展示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 增加搜索条件
    search_fields = ['code', 'email', 'send_type']
    # list_filter表示要增加过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 完成这个表的注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSetting)

