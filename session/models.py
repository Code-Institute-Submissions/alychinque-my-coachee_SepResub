from profiles.models import Coachee, Coach
from indications.models import Indication
from django.db import models

class Session(models.Model):
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.SET_NULL)
    coachee = models.ForeignKey(Coachee, null=True, blank=True, on_delete=models.SET_NULL)
    session = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    jornal = models.TextField(null=True, blank=True)
    indications1 = models.ForeignKey(Indication, related_name="indication1", null=True, blank=True, on_delete=models.SET_NULL)
    indications2 = models.ForeignKey(Indication, related_name="indication2", null=True, blank=True, on_delete=models.SET_NULL)
    indications3 = models.ForeignKey(Indication, related_name="indication3", null=True, blank=True, on_delete=models.SET_NULL)
    concluded = models.BooleanField()

    def __str__(self):
    	return ('Session with ' + self.coachee.name + ' on ' + str(self.date) + ' at ' + str(self.time))

class Report_Session(models.Model):
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.SET_NULL)
    hours_session = models.IntegerField()
    appointments = models.IntegerField()

    def __str__(self):
    	return (self.coach.name + ' spent ' + self.hours_session + ' hours in sessions and has ' + self.appointments + ' appointmemts')
