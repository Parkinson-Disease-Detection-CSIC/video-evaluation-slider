from django.db import models

class Evaluation(models.Model):
    evaluator = models.CharField(db_index=True, max_length=40)
    general_date = models.DateTimeField('evaluation date for general')
    symptoms_date = models.DateTimeField('evaluation date for symptoms')
    subject = models.IntegerField(db_index=True)
    time_spent_general = models.IntegerField()
    time_spent_symptoms = models.IntegerField()
    done_general = models.BooleanField(default=False)
    done_symptoms = models.BooleanField(default=False)
    tremor = models.FloatField()
    tremor_confidence = models.IntegerField()
    bradykinesia = models.FloatField()
    bradykinesia_confidence = models.IntegerField()
    stability = models.FloatField()
    stability_confidence = models.IntegerField()
    dyn_stability = models.FloatField()
    dyn_stability_confidence = models.IntegerField()
    freezing = models.FloatField()
    freezing_confidence = models.IntegerField()
    smoothness = models.FloatField()
    smoothness_confidence = models.IntegerField()
    symmetry = models.FloatField()
    symmetry_confidence = models.IntegerField()
    general = models.FloatField()
    general_confidence = models.IntegerField()

    class Meta:
        unique_together = ('evaluator', 'subject')

    def __str__(self):
        return self.evaluator + " " + str(self.subject) + " " + str(self.date)
