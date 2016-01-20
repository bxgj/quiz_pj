from django.conf.urls import url
from quiz.views import QuestionList, QuestionCreate, QuestionDetail,QuestionUpdate
# from django.views.generic import TemplateView

urlpatterns = [
    # url(r'', TemplateView.as_view(template_name='quiz/index.html'), name='index'),
    url(r'^$', QuestionList.as_view(), name='question-list'),
    url(r'^(?P<pk>[0-9]+)/$', QuestionDetail.as_view(), name='question-detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', QuestionUpdate.as_view(), name='question-edit'),
    url(r'^new$', QuestionCreate.as_view(), name='question-new'),
]
