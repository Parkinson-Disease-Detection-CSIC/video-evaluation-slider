from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Evaluation
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .videos import video_urls
from .queries import get_list_remaining_evaluations
from .queries import update_symptoms_evaluation
from .queries import update_general_evaluation
import random

@login_required
def index(request):
    return redirect_random(request)

def get_all_evaluations():
    return [
        (subject, type)
        for subject in video_urls for type in ['general', 'symptoms']
    ]

def redirect_random(request):
    all_evaluations = get_all_evaluations()
    remaining_evaluations = get_list_remaining_evaluations(request.user, all_evaluations)
    if len(remaining_evaluations) > 0:
        random_index = random.randrange(len(remaining_evaluations))
        random_evaluation = remaining_evaluations[random_index]
        return redirect(f"/polls/{random_evaluation[0]}/{random_evaluation[1]}/details")
    else:
        return render(request, 'polls/congratulations.html', {})

@login_required
def backwards_redirect(request, sub_num):
    return redirect_random(request)

@login_required
def details(request, sub_num, input_type):
    try:
        evaluation = Evaluation.objects.get(pk=sub_num)
    except Evaluation.DoesNotExist:
        evaluation = None
    all_evaluations = get_all_evaluations()
    remaining_evaluations = get_list_remaining_evaluations(request.user, all_evaluations)
    parameters = {
        'evaluation': evaluation,
        'evaluations_done': len(all_evaluations) - len(remaining_evaluations),
        'total_evaluations': len(all_evaluations),
	'sub_num': sub_num,
	'videos': list(video_urls[sub_num].values()),
	'type': input_type
    }
    return render(request, 'polls/detail.html', parameters)

@login_required
def evaluate(request, sub_num, input_type):
    if input_type == 'general':
        update_general_evaluation(
            request.user,
            sub_num,
            int(request.POST.get('rangeGeneral')),
            int(request.POST.get('rateGeneral')),
            int(float(request.POST.get('time_spent')))
        )
    else:
        symptoms = {
            key: int(request.POST.get(key))
            for key in request.POST if key != 'csrfmiddlewaretoken' and key != 'time_spent'
        }
        update_symptoms_evaluation(
            request.user,
            sub_num,
            symptoms,
            int(float(request.POST.get('time_spent')))
        )
    return redirect_random(request)
