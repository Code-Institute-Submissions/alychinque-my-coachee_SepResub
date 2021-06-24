from profiles.models import Coachee
from indications.models import Indication
from django.db import models

class Session(models.Model):
    coach = models.ForeignKey('Coach', null=True, blank=True, on_delete=models.SET_NULL)
    coachee = models.ForeignKey('Coachee', null=True, blank=True, on_delete=models.SET_NULL)
    session = models.IntegerField()
    date_time = models.DateTimeField()
    jornal = models.TextField()
    indications1 = models.ForeignKey('Indications', null=True, blank=True, on_delete=models.SET_NULL)
    indications2 = models.ForeignKey('Indications', null=True, blank=True, on_delete=models.SET_NULL)
    indications3 = models.ForeignKey('Indications', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
    	return self.session

class Report_Session(models.Model):
    coach = models.ForeignKey('Coach', null=True, blank=True, on_delete=models.SET_NULL)
    hours_session = models.TimeField
    appointments = models.IntegerField()

    def __str__(self):
    	return self.hours_session + ' ' + self.appointments
