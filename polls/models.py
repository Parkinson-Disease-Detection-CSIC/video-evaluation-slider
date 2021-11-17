from django.db import models

class Evaluation(models.Model):
    evaluator = models.CharField(db_index=True, max_length=40)
    date = models.DateTimeField('evaluation date')
    subject = models.IntegerField(db_index=True)
    time_spent_general = models.IntegerField()
    time_spent_symptoms = models.IntegerField()
    tremor = models.FloatField()
    bradykinesia = models.FloatField()
    stability = models.FloatField()
    dyn_stability = models.FloatField()
    freezing = models.FloatField()
    smoothness = models.FloatField()
    symmetry = models.FloatField()
    general = models.FloatField()

    def __str__(self):
        return self.evaluator + " " + str(self.subject) + " " + str(self.date)
