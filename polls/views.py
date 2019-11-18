from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    return HttpResponse("Welcome on my index page")


def hello(request):
    return HttpResponse("Hello world")


def question_list(request):
    questions = Question.objects.all()
    # template = loader.get_template('123.html')
    context = {
        'questions': questions
    }
    # return HttpResponse(template.render(context, request))
    return render(
        request,
        template_name='polls/list.html',
        context=context
    )


class ListView(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'polls/list.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # template = loader.get_template('detail_123.html')
    context = {
        'question': question
    }
    print(context)
    # return HttpResponse(template.render(context, request))
    return render(
        request,
        template_name='polls/detail.html',
        context=context
    )


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        template_name='polls/results.html',
        context={
            'question': question}
    )
    # return HttpResponse(f"Wyniki glosowania: {question_id}")


class ResultView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.pub_date > timezone.now():
        raise Http404
    choice_id = request.POST.get('choice')
    try:
        selected_choice = question.choice_set.get(pk=choice_id)

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            template_name='polls/detail.html',
            context={
                'question': question,
                'error_message': 'niewybrano odpowiedzi'}
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # topla argument id z przecinkiem

    # return HttpResponse(f"glosuje w pytaniu: {question_id}")
