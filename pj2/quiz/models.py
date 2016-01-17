# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text=models.CharField('问题',max_length=100)
    QUESTION_CATEGORY_CHOICES=(('EJ','娱乐'),('LF','生活'),('HI','历史'),('EC','经济'),('PO','政治'),('CU','文化'),('PH','物理'),('CH','化学'),('BI','生物'),('IT','技术'),('OT','其它'))
    question_category=models.CharField('分类',max_length=20,choices=QUESTION_CATEGORY_CHOICES,default='OT')
    question_score=models.IntegerField('分值', validators=[MaxValueValidator(100,'超出最大值 100'),MinValueValidator(0,'超出最小值 0')],help_text="分值在0~100之间")
    question_limit_second=models.IntegerField('限时/秒',default=20)
    question_solver=models.ManyToManyField('Consumer',verbose_name='参与者',blank=True)
    question_creater=models.ForeignKey('Supplier', verbose_name='创建者')
    question_create_at=models.DateTimeField('创建时间',default=timezone.now)
    question_close_at=models.DateTimeField('关闭时间',default=datetime.datetime.now() + datetime.timedelta(hours=8))

    def question_level(self):
        easy_range=range(0,31)
        normal_range=range(31,61)
        hard_range=range(61,91)
        very_hard_range=range(91,101)
        if self.question_score in easy_range:
            level='简单'
        elif self.question_score in normal_range:
            level='普通'
        elif self.question_score in hard_range:
            level='困难'
        elif self.question_score in very_hard_range:
            level='极难'
        else:
            level=''
        return level

    def __unicode__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('update',kwargs={'pk':self.pk})

    class Meta:
        verbose_name='问题库'
        verbose_name_plural='问题库'

class Choice(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    choice_text=models.CharField('选项',max_length=50)
    iscorrect=models.BooleanField('是否正确答案')
    def __unicode__(self):
        return self.choice_text
    class Meta:
        verbose_name='问题选项'
        verbose_name_plural='问题选项'

class Player(models.Model):
    player_name=models.CharField('玩家名称',max_length=50,unique=True)
    player_password=models.CharField('密码',max_length=50)
    player_score=models.IntegerField('得分',default=0)
    rank=models.IntegerField('排名',default=0)
    ROLE_CHOICES=(('S','创建者'),('C','参与者'),('A','创建者和参与者'))
    role=models.CharField('角色',max_length=20, choices=ROLE_CHOICES,default='C')
    def __unicode__(self):
        return self.player_name
    class Meta:
        verbose_name='玩家'
        verbose_name_plural='玩家'

class Consumer(Player):
    answer_count=models.IntegerField('回答总数',default=0)
    success_count=models.IntegerField('回答正确数',default=0)
    fail_count=models.IntegerField('回答错误数',default=0)
    class Meta:
        verbose_name='问题参与者'
        verbose_name_plural='问题参与者'

class Supplier(Player):
    create_count=models.IntegerField('问题创建数',default=0)
    class Meta:
        verbose_name='问题创建者'
        verbose_name_plural='问题创建者'

