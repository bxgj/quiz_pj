from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from quiz.models import Question

def index(request):
    welcome="welcome to visit quiz"
    return render(request,'quiz/index.html',{'welcome':welcome})

class QuestionList(ListView):
	model=Question
	context_object_name="question_list"
	template_name="quiz/index.html"

