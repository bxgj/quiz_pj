# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20151229_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_close_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 16, 45, 0, 947452), verbose_name='\u5173\u95ed\u65f6\u95f4'),
        ),
    ]
