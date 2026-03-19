from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    return HttpResponse(f"To jest pytanie nr {question_id}")