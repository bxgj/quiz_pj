from django.conf.urls import url
from quiz.views import QuestionList, QuestionCreate
# from django.views.generic import TemplateView

urlpatterns = [
    # url(r'', TemplateView.as_view(template_name='quiz/index.html'), name='index'),
    url(r'^$', QuestionList.as_view(), name='question-list'),
    url(r'^new$', QuestionCreate.as_view(), name='question-new'),
]
