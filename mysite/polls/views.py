from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list' #Returned by queryset

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    context_object_name = 'question' # name of object used in context
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'result.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.vote += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #Redirect is the best pratice in web develop after dealing wit post metod

"""

Without Generic Viws
from select import select
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from django.template import loader


from .models import Choice, Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html') #old way
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("--------------------------------")
    print(f"question :{question}")
    print("--------------------------------")
    return render(request, 'result.html',{'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.vote += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #Redirect is the best pratice in web develop after dealing wit post metod


"""