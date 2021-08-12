from profiles.models import Coachee, Coach
from indications.models import Indication
from django.db import models

class AppointmentSession(models.Model):
    coach = models.ForeignKey(Coach, null=False, blank=False, on_delete=models.CASCADE)
    coachee = models.ForeignKey(Coachee, null=False, blank=False, on_delete=models.CASCADE)
    number_session = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)

    def __str__(self):
    	return f'Coach {self.coach.name} session with {self.coachee.name} on {self.date} at {self.time}.'

class Session(models.Model):
    appointment_session = models.ForeignKey(AppointmentSession, null=False, blank=False, on_delete=models.CASCADE)
    jornal = models.TextField(null=False, blank=False)
    indications1 = models.ForeignKey(Indication, related_name="indication1", null=False, blank=False, on_delete=models.CASCADE)
    indications2 = models.ForeignKey(Indication, related_name="indication2", null=False, blank=False, on_delete=models.CASCADE)
    indications3 = models.ForeignKey(Indication, related_name="indication3", null=False, blank=False, on_delete=models.CASCADE)
    concluded = models.BooleanField(null=False, blank=False)

    def  __str__(self):
	    return self.name