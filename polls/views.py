from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render

from polls.models import Question


def index(request):
    top5_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "top5_questions": top5_questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists.")
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
