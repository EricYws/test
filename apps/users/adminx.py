#_*_ encoding:utf-8 _*_

import xadmin

from .models import EmailVerifyRecord

class EmailVerifyRecordAdmin(object):
    pass

#完成这个表的注册
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)