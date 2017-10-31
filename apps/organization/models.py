#_*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc=models.CharField(max_length=200,verbose_name=u"城市描述")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"城市"
        verbose_name_plural=verbose_name


class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name=u"机构名称")
    desc=models.TextField(verbose_name=u"机构描述")
    click_num=models.IntegerField(default=0,verbose_name=u"点击数")
    fav_num=models.IntegerField(default=0,verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图")
    address=models.CharField(max_length=150,verbose_name=u"地址")
    city=models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程机构"
        verbose_name_plural=verbose_name


class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,u"机构名称")
    name=models.CharField(max_length=50,verbose_name="教师名")
    work_time=models.IntegerField(default=0,verbose_name=u"工作时间")
    work_company=models.CharField(max_length=50,verbose_name=u"就职公司")
    work_position=models.CharField(max_length=50,verbose_name=u"公司职位")
    points=models.CharField(max_length=200,verbose_name=u"教学特点")
    fav_num=models.IntegerField(default=0,verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"教师"
        verbose_name_plural=verbose_name






