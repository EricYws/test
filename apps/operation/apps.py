# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class OperationConfig(AppConfig):
    # name = 'operation'
    verbose_name=u"用户操作"

default_app_config = 'operation.apps.OperationConfig'