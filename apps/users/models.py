#_*_ encoding:utf-8 _*_
from __future__ import unicode_literals
#第一块区域import python自带的
from datetime import datetime

#第二块区域import 第三方（例如django）
from django.db import models
from django.contrib.auth.models import AbstractUser

#第三块区域import 自己定义的，每个区域之间用一行隔开

#在AbstractUser的基础上创建新的表
# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(("male", u"男"), ("female", u"女")), default="")
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to="image/%Y/%m", default=u"image/default.png")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


#邮箱验证码
class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    #定义一个邮箱状态，注册和找回密码
    send_type=models.CharField(verbose_name=u"验证码类型",max_length=10,choices=(("register",u"注册"),("forget",u"找回密码")))
    send_time=models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


#轮播图
class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图")
    url=models.URLField(max_length=200,verbose_name=u"访问地址")
    index=models.IntegerField(default=100,verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name
