# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20151229_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_close_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 23, 52, 12, 453027), verbose_name='\u5173\u95ed\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_level',
            field=models.CharField(blank=True, default=b'<property object at 0x10639a0a8>', max_length=50, null=True, verbose_name='\u96be\u5ea6'),
        ),
    ]
