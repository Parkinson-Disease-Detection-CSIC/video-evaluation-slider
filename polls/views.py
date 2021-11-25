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
    user = authenticate()
    return redirect_random(user)

def get_all_evaluations():
    return [
        (subject, type)
        for subject in video_urls for type in ['general', 'symptoms']
    ]

def redirect_random(user):
    all_evaluations = get_all_evaluations()
    remaining_evaluations = get_list_remaining_evaluations(user, all_evaluations)
    random_index = random.randrange(len(remaining_evaluations))
    random_evaluation = remaining_evaluations[random_index]
    return redirect(f"/polls/{random_evaluation[0]}/{random_evaluation[1]}/details")

@login_required
def backwards_redirect(request, sub_num):
    return redirect_random(user)

@login_required
def details(request, sub_num, input_type):
    user = authenticate()
    try:
        evaluation = Evaluation.objects.get(pk=sub_num)
    except Evaluation.DoesNotExist:
        evaluation = None
    all_evaluations = get_all_evaluations()
    remaining_evaluations = get_list_remaining_evaluations(user, all_evaluations)
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
    user = authenticate()
    if input_type == 'general':
        update_general_evaluation(
            user,
            sub_num,
            request.POST.get('rangeGeneral'),
            request.POST.get('rateGeneral'),
            request.POST.get('time_spent')
        )
    else:
        symptoms = {
            key: request.POST.get(key)
            for key in request.POST if key != 'csrfmiddlewaretoken'
        }
        update_symptoms_evaluation(
            user,
            sub_num,
            symptoms,
            request.POST.get('time_spent')
        )
    return redirect_random(user)
