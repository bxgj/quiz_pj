from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Question(models.Model):
    question_text=models.CharField(max_length=20)
    pub_date=models.DateField(default=timezone.now())
    class Meta:
         ordering = [ "-pub_date"] 
    def __unicode__(self):
        return self.question_text
    def get_absolute_url(self):
            return reverse('question-detail', kwargs={'pk': self.pk})   
            # for template to use object.get_absolute_url to show the question-detail, instead of function url in template

class Choice(models.Model):
    choice_text=models.CharField(max_length=20)
    question=models.ForeignKey('Question',on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.choice_text
