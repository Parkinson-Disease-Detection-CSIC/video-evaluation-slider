from .models import Evaluation
from datetime import datetime

def get_list_remaining_evaluations(user, all_evaluations):
    q = Evaluation.objects.filter(
        evaluator=user
    )
    evaluations_done = list(q)
    evaluated_general_list = [
        (eval.subject, 'general')
	for eval in evaluations_done
	if eval.done_general
    ]
    evaluated_symptoms_list = [
        (eval.subject, 'symptoms')
	for eval in evaluations_done
	if eval.done_symptoms
    ]
    evaluated_list = evaluated_general_list + evaluated_symptoms_list
    return [
        (subject, type)
        for (subject, type) in all_evaluations
        if (subject, type) not in evaluated_list
    ]

def update_eval_general(eval, general, confidence, time_spent):
    eval.general_date = datetime.now()
    eval.time_spent_general = time_spent
    eval.done_general = True
    eval.general = general
    eval.general_confidence = confidence
    return eval

def update_general_evaluation(user, subject, general, confidence, time_spent):
    try:
        eval = Evaluation.objects.get(
            evaluator = user,
            subject = subject
        )
    except Evaluation.DoesNotExist:
        eval = Evaluation(
            evaluator = user,
            subject = subject
        )
    eval = update_eval_general(eval, general, confidence, time_spent)
    return eval.save()

def update_eval_symptoms(eval, symptoms, time_spent):
    eval.time_spent_symptoms = time_spent
    eval.symptoms_date = datetime.now()
    eval.done_symptoms = True
    eval.tremor = symptoms['rangeTremor']
    eval.tremor_confidence = symptoms['rateTremor']
    eval.bradykinesia = symptoms['rangeBradykinesia']
    eval.bradykinesia_confidence = symptoms['rateBradykinesia']
    eval.stability = symptoms['rangeStability']
    eval.stability_confidence = symptoms['rateStability']
    eval.dyn_stability = symptoms['rangeDynStability']
    eval.dyn_stability_confidence = symptoms['rateDynStability']
    eval.freezing = symptoms['rangeFreezing']
    eval.freezing_confidence = symptoms['rateFreezing']
    eval.smoothness = symptoms['rangeSmoothness']
    eval.smoothness_confidence = symptoms['rateSmoothness']
    eval.symmetry = symptoms['rangeSymmetry']
    eval.symmetry_confidence = symptoms['rateSymmetry']
    return eval

def update_symptoms_evaluation(user, subject, symptoms, time_spent):
    try:
        eval = Evaluation.objects.get(
            evaluator = user,
            subject = subject
        )
    except Evaluation.DoesNotExist:
        eval = Evaluation(
            evaluator = user,
            subject = subject
        )
    eval = update_eval_symptoms(eval, symptoms, time_spent)
    return eval.save()
