from django.shortcuts import render
from quiz.models import Question, Choice
from django.views.generic import ListView, DetailView, CreateView,UpdateView
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
	def get_success_url(self):
		return reverse('question-list')

class QuestionUpdate(UpdateView):
    models=Question
    fields=['question_text',]
    template_name='quiz/question_edit.html'
    def get_queryset(self):
        queryset=Question.objects.filter(pk=self.kwargs['pk'])
        # get return object, filter return queryset, here can not use get
        return queryset
    def get_success_url(self):
        return reverse('question-list')
