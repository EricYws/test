# _*_ encoding:utf-8 _*_

import xadmin

from .models import CourseOrg,CityDict,Teacher

class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display=['name','desc','click_nums','fav_nums']
    search_fields=['name','desc','click_nums','fav_nums']
    list_filter=['name','desc','click_nums','fav_nums']

class TeacherAdmin(object):
    list_display=['org','name','work_years','work_conpany']
    search_fields=['org','name','work_years','work_conpany']
    list_filter=['org','name','work_years','work_conpany']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)