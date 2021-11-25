from django.db import models

class Evaluation(models.Model):
    evaluator = models.CharField(db_index=True, max_length=40)
    subject = models.IntegerField(db_index=True)
    done_general = models.BooleanField(default=False)
    done_symptoms = models.BooleanField(default=False)
    general_date = models.DateTimeField('evaluation date for general', default=None, blank=True, null=True)
    symptoms_date = models.DateTimeField('evaluation date for symptoms', default=None, blank=True, null=True)
    time_spent_general = models.IntegerField(default=None, blank=True, null=True)
    time_spent_symptoms = models.IntegerField(default=None, blank=True, null=True)
    tremor = models.FloatField(default=None, blank=True, null=True)
    tremor_confidence = models.IntegerField(default=None, blank=True, null=True)
    bradykinesia = models.FloatField(default=None, blank=True, null=True)
    bradykinesia_confidence = models.IntegerField(default=None, blank=True, null=True)
    stability = models.FloatField(default=None, blank=True, null=True)
    stability_confidence = models.IntegerField(default=None, blank=True, null=True)
    dyn_stability = models.FloatField(default=None, blank=True, null=True)
    dyn_stability_confidence = models.IntegerField(default=None, blank=True, null=True)
    freezing = models.FloatField(default=None, blank=True, null=True)
    freezing_confidence = models.IntegerField(default=None, blank=True, null=True)
    smoothness = models.FloatField(default=None, blank=True, null=True)
    smoothness_confidence = models.IntegerField(default=None, blank=True, null=True)
    symmetry = models.FloatField(default=None, blank=True, null=True)
    symmetry_confidence = models.IntegerField(default=None, blank=True, null=True)
    general = models.FloatField(default=None, blank=True, null=True)
    general_confidence = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        unique_together = ('evaluator', 'subject')

    def __str__(self):
        return self.evaluator + " " + str(self.subject) + " " + str(self.date)
