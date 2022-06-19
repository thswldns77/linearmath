from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import  Choice, Question, Exam
from django.http import Http404

def index(request):
    latest_exam_list = Exam.objects.order_by()
    return render(request,'polls/index.html', {'latest_exam_list': latest_exam_list})

def problem(request, exam_id):
    exam = get_object_or_404(Exam, pk= exam_id)
    return render(request,'polls/problem.html',{'exam':exam})


def detail(request, exam_id):
    exam = get_object_or_404(Exam, pk= exam_id)

    return render(request, 'polls/detail.html',{'exam':exam})

def results(request, exam_id, score):
    exam = get_object_or_404(Exam, pk= exam_id)

    return render(request, 'polls/results.html',{'exam':exam ,'score':score})


def score(request, exam_id):
    exam = get_object_or_404(Exam, pk= exam_id)
    selected_choices = []
    score = 0
    num = 0
    try:
        for question in exam.question_set.all():
            selected_choices.append(question.choice_set.get(pk=request.POST[question.question_text])) 
            num += 1
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'exam': exam,'error_message': "You didn't select a choice.",})
    else:
        for i in selected_choices:
            i.votes += 1
            i.save()
            if i.answer == True:
                score += 100/num
        return render(request,'polls/results.html',{'exam': exam, 'score':round(score,2)} )