# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20151229_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='_question_level',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u96be\u5ea6'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_close_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 23, 12, 42, 94792), verbose_name='\u5173\u95ed\u65f6\u95f4'),
        ),
    ]
