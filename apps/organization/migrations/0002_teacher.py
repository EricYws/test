# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-01 03:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6559\u5e08\u540d')),
                ('work_years', models.IntegerField(default=0, verbose_name='\u5de5\u4f5c\u5e74\u9650')),
                ('work_conpany', models.CharField(max_length=50, verbose_name='\u5c31\u804c\u516c\u53f8')),
                ('work_position', models.CharField(max_length=50, verbose_name='\u516c\u53f8\u804c\u4f4d')),
                ('points', models.CharField(max_length=50, verbose_name='\u6559\u5b66\u7279\u70b9')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u6240\u5c5e\u673a\u6784')),
            ],
            options={
                'verbose_name': '\u6559\u5e08',
                'verbose_name_plural': '\u6559\u5e08',
            },
        ),
    ]
