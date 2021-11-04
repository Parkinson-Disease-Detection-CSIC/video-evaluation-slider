from django.http import HttpResponse
from django.shortcuts import render
from .models import Evaluation
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("This is a video evaluator app for Parkinson's symptoms.")

@login_required
def results(request):
    return HttpResponse("You're looking at all subjects.")

@login_required
def detail(request, sub_num):
    user = authenticate()
    try:
        evaluation = Evaluation.objects.get(pk=sub_num)
    except Evaluation.DoesNotExist:
        evaluation = None
    parameters = {
        'evaluation': evaluation,
	'sub_num': sub_num,
    }
    return render(request, 'polls/detail.html', parameters)

@login_required
def evaluate(request, sub_num):
    return HttpResponse("You're evaluating subject %s." % sub_num)
