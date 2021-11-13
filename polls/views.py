from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Evaluation
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .videos import video_urls
import random

@login_required
def index(request):
    return redirect('/polls/68/general/details')

def handler404(request):
    return redirect('/polls/68/general/details')

@login_required
def details(request, sub_num, input_type):
    user = authenticate()
    try:
        evaluation = Evaluation.objects.get(pk=sub_num)
    except Evaluation.DoesNotExist:
        evaluation = None
    parameters = {
        'evaluation': evaluation,
        'evaluations_done': random.randint(0, 22),
        'total_evaluations': random.randint(120, 200),
	'sub_num': sub_num,
	'videos': list(video_urls[sub_num].values()),
	'type': input_type
    }
    return render(request, 'polls/detail.html', parameters)

@login_required
def evaluate(request, sub_num, input_type):
    user = authenticate()
    if request.method == 'POST':
        if sub_num == 66:
           new_sub_num = 68
        else:
           new_sub_num = 66
        if input_type == "general":
           new_type = "symptoms"
        else:
           new_type = "general"
        return redirect(f"/polls/{new_sub_num}/{new_type}/details")
    return redirect('/polls/68/general/details')
