from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    top5_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "top5_questions": top5_questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
