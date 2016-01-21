from django.shortcuts import render
from quiz.models import Question, Choice
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
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
    context_object_name='myquestion' #default is "object" or "question"
    def get_success_url(self):
        return reverse('question-list')

class QuestionUpdate(UpdateView):
    models=Question
    fields=['question_text',]
    template_name='quiz/question_edit.html'
    context_object_name='myquestion'
    success_url=reverse_lazy('question-list')
    # if not defind success_url will only redirect to question-detail 
    def get_queryset(self):
        queryset=Question.objects.filter(pk=self.kwargs['pk'])
        return queryset

class QuestionDelete(DeleteView):
    models=Question
    template_name='quiz/question_delete.html'
    success_url=reverse_lazy('question-list')
    def get_queryset(self):
        queryset=Question.objects.filter(pk=self.kwargs['pk'])
        return queryset
