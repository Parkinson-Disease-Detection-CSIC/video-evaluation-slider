from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Evaluation
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .videos import get_video_urls
from .queries import get_list_remaining_evaluations
from .queries import update_symptoms_evaluation
from .queries import update_general_evaluation
from .queries import get_all_data
import csv
import random

def get_all_evaluations():
    return [
        (subject, type)
        for subject in get_video_urls() for type in ['general', 'symptoms']
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
def index(request):
    evaluators = request.GET.get('evaluators')
    if evaluators is None:
        return redirect_random(request)
    else:
        return make_report(evaluators.split(","))

def make_report(evaluators):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="evaluations.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow([
        'evaluator',
        'subject',
        'general',
        'tremor',
        'bradykinesia',
        'stability',
        'dyn_stability',
        'freezing',
        'smoothness',
        'symmetry',
        'general_date',
        'symptoms_date',
        'time_spent_general',
        'time_spent_symptoms',
        'general_confidence',
        'tremor_confidence',
        'bradykinesia_confidence',
        'stability_confidence',
        'dyn_stability_confidence',
        'freezing_confidence',
        'smoothness_confidence',
        'symmetry_confidence'
    ])
    for eval in get_all_data(evaluators):
        row = [
           eval.evaluator,
           eval.subject,
           eval.general,
           eval.tremor,
           eval.bradykinesia,
           eval.stability,
           eval.dyn_stability,
           eval.freezing,
           eval.smoothness,
           eval.symmetry,
           eval.general_date,
           eval.symptoms_date,
           eval.time_spent_general,
           eval.time_spent_symptoms,
           eval.general_confidence,
           eval.tremor_confidence,
           eval.bradykinesia_confidence,
           eval.stability_confidence,
           eval.dyn_stability_confidence,
           eval.freezing_confidence,
           eval.smoothness_confidence,
           eval.symmetry_confidence
        ]
        writer.writerow(row)
    return response

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
	'videos': list(get_video_urls()[sub_num].values()),
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
