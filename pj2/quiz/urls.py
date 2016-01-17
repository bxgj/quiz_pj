from django.conf.urls import url
from quiz.views import QuestionList

urlpatterns = [
        url(r'^quiz/$', QuestionList.as_view(),name='index'),
]