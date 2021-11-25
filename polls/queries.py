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

def update_general_evaluation(user, subject, general, confidence, time_spent):
    eval = Evaluation(
        evaluator = user,
        general_date = datetime.now(),
        subject = subject,
        time_spent_general = time_spent,
        done_general = True,
        general = general,
        general_confidence = confidence,
    )
    return eval.save()

def update_symptoms_evaluation(user, subject, symptoms, time_spent):
    eval = Evaluation(
        evaluator = user,
        symptoms_date = datetime.now(),
        subject = subject,
        time_spent_symptoms = time_spent,
        done_symptoms = True,
        tremor = symptoms['rangeTremor'],
        tremor_confidence = symptoms['rateTremor'],
        bradykinesia = symptoms['rangeBradykinesia'],
        bradykinesia_confidence = symptoms['rateBradykinesia'],
        stability = symptoms['rangeStability'],
        stability_confidence = symptoms['rateStability'],
        dyn_stability = symptoms['rangeDynStability'],
        dyn_stability_confidence = symptoms['rateDynStability'],
        freezing = symptoms['rangeFreezing'],
        freezing_confidence = symptoms['rateFreezing'],
        smoothness = symptoms['rangeSmoothness'],
        smoothness_confidence = symptoms['rateSmoothness'],
        symmetry = symptoms['rangeSymmetry'],
        symmetry_confidence = symptoms['rateSymmetry'],
    )
    return eval.save()
