from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from quiz.models import Question,Choice,Player
from django.forms import inlineformset_factory, ModelForm, CheckboxInput, Select
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    welcome="welcome to visit quiz"
    return render(request,'quiz/index.html',{'welcome':welcome})

class QuestionList(ListView):
    model=Question
    context_object_name="question_list"
    template_name="quiz/index.html"
    def get_context_data(self,**kwargs):
        context = super(QuestionList,self).get_context_data(**kwargs)
        context['player_list'] = Player.objects.all()
        return context

# class QuestionDetail(DetailView):
#     model=Question
#     context_object_name="question_object"
#     template_name='quiz/detail.html'
#     def get_context_data(self, **kwargs):
#         context = super(QuestionDetail, self).get_context_data(**kwargs)
#         question=context['question_object']
#         choice_formset=question.choice_set.all()
#         context['choice_formset'] = choice_formset
#         return context
class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields='__all__'

class QuestionDetail(DetailView):
    model=Question
    context_object_name="question_object"
    template_name='quiz/detail.html'
    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        question_id=context['question_object'].id
        # ChoiceFormSet=inlineformset_factory(Question,Choice,fields=('choice_text',),extra=0,widgets={"choice_text":Select()})
        ChoiceFormSet=inlineformset_factory(Question,Choice,fields=('choice_text',),extra=0)
        question=Question.objects.get(pk=question_id)
        choice_formset=ChoiceFormSet(instance=question)
        context['choice_formset'] = choice_formset
        return context

class QuestionCreate(CreateView):
    model=Question
    fields=['question_text','question_score']
    # template_name="quiz/add.html"
    success_url=reverse_lazy('index')
    # form_class=QuestionForm

class QuestionUpdate(UpdateView):
    model=Question
    fields=['question_text','question_score']
    success_url=reverse_lazy('index')

class QuestionDelete(DeleteView):
    model=Question
    success_url=reverse_lazy('index')



# def addQuestion(request):
#     form = QuestionForm()
#     return render(request, 'quiz/add.html', {'form': form})


# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#         else:
#             form = NameForm()
#         return render(request, 'name.html', {'form': form})






