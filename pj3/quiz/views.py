from django.shortcuts import render
from quiz.models import Question, Choice
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy, reverse

class QuestionList(ListView):
	model=Question
	template_name='quiz/question_list.html'
	context_object_name='question_list'

class QuestionDetail(DetailView):
	model=Question
	template_name='quiz/question_detail.html'
	context_object_name='question_object'

class QuestionCreate(CreateView):
	model=Question
	fields='__all__'
	template_name='quiz/question_edit.html'
	# success_url=reverse_lazy('question_list') # do not use this one, many problems
	# whild call this class view , show the form to edit, form name is "form" as default
	def get_success_url(self):
		return reverse('question-list') 
		# while success submit the form , jump to list page to advoid repeat submit