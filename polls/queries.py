from .models import Evaluation

def get_list_remaining_evaluations(user, all_evaluations):
    q = Evaluation.objects.filter(
        user=user
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
        tremor = symptoms['tremor'].value,
        tremor_confidence = symptoms['tremor'].confidence,
        bradykinesia = symptoms['bradykinesia'].value,
        bradykinesia_confidence = symptoms['bradykinesia'].confidence,
        stability = symptoms['stability'].value,
        stability_confidence = symptoms['stability'].confidence,
        dyn_stability = symptoms['dyn_stability'].value,
        dyn_stability_confidence = symptoms['dyn_stability'].confidence,
        freezing = symptoms['freezing'].value,
        freezing_confidence = symptoms['freezing'].confidence,
        smoothness = symptoms['smoothness'].value,
        smoothness_confidence = symptoms['smoothness'].confidence,
        symmetry = symptoms['symmetry'].value,
        symmetry_confidence = symptoms['symmetry'].confidence,
    )
    return eval.save()
