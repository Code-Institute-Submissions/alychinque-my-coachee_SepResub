from profiles.models import Coachee, Coach
from indications.models import Indication
from django.db import models

class AppointmentSession(models.Model):
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.CASCADE)
    coachee = models.ForeignKey(Coachee, null=True, blank=True, on_delete=models.CASCADE)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
    	return f'Coach {self.coach.name} session with {self.coachee.name} on {self.date} at {self.time}.'

class Session(models.Model):
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.CASCADE)
    coachee = models.ForeignKey(Coachee, null=True, blank=True, on_delete=models.CASCADE)
    session = models.IntegerField()
    jornal = models.TextField(null=True, blank=True)
    indications1 = models.ForeignKey(Indication, related_name="indication1", null=True, blank=True, on_delete=models.CASCADE)
    indications2 = models.ForeignKey(Indication, related_name="indication2", null=True, blank=True, on_delete=models.CASCADE)
    indications3 = models.ForeignKey(Indication, related_name="indication3", null=True, blank=True, on_delete=models.CASCADE)
    concluded = models.BooleanField()

    def __str__(self):
    	return f'Coach {self.coach.name} session number {self.session} with {self.coachee.name}.'
