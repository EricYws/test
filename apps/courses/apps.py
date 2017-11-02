# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'
    verbose_name=u"课程管理"

default_app_config = 'courses.apps.CoursesConfig'
