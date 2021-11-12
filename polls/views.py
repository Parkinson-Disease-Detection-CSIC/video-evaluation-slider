from django.http import HttpResponse
from django.shortcuts import render
from .models import Evaluation
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .videos import video_urls

def index(request):
    return HttpResponse("This is a video evaluator app for Parkinson's symptoms.")

@login_required
def results(request):
    return HttpResponse("You're looking at all subjects.")

@login_required
def general(request, sub_num):
    return detail(request, 66, 'general')

@login_required
def symptoms(request, sub_num):
    return detail(request, 68, 'symptoms')

def detail(request, sub_num, type):
    user = authenticate()
    try:
        evaluation = Evaluation.objects.get(pk=sub_num)
    except Evaluation.DoesNotExist:
        evaluation = None
    parameters = {
        'evaluation': evaluation,
	'sub_num': sub_num,
	'videos': list(video_urls[sub_num].values()),
	'type': type
    }
    return render(request, 'polls/detail.html', parameters)

@login_required
def evaluate(request, sub_num):
    return HttpResponse("You're evaluating subject %s." % sub_num)
