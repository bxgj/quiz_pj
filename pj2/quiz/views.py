from django.views.generic import ListView
from quiz.models import Question

class QuestionList(ListView):
	model='Question'
	template_name='quiz/index.html'
	context_object_name='question_list'

