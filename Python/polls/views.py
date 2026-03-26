from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = request.POST.get('choice')

    try:
        choice = question.choice_set.get(pk=selected_choice)
    except:
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Nie wybrano opcji",
        })

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(
        reverse("polls:results", args=(question.id,))
    )