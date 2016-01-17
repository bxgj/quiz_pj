"""pj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from quiz.views import QuestionList,QuestionDetail,QuestionCreate,QuestionUpdate,QuestionDelete,QuestionForm
from django.views.generic import TemplateView
app_name='quiz'
urlpatterns = [
        url(r'^quiz/$', QuestionList.as_view(),name='index'),
        url(r'^quiz/add/$', QuestionCreate.as_view(),name='add'),
        url(r'^quiz/update/(?P<pk>\d+)/$', QuestionUpdate.as_view(),name='update'),
        url(r'^quiz/delete/(?P<pk>\d+)/$', QuestionDelete.as_view(),name='delete'),
        url(r'^quiz/(?P<pk>\d+)/$', QuestionDetail.as_view(),name='detail'),
        # url(r'^quiz/aa/$', 'quiz.views.addQuestion',name='aa'),
        # url(r'^quiz/detail/$', TemplateView.as_view(template_name='quiz/detail.html'),name='detail'),
]
