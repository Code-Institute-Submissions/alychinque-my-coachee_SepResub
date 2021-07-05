from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Full Name', null=False, blank=False)
    date_of_birth = models.DateField(verbose_name='Date Of Birth', null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    list_gender = (
        ("male", "M"),
        ("female", "F"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=8, choices=list_gender, verbose_name='Gender')

    class Meta:
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'

    def  __str__(self):
	    return self.name

class Coachee(models.Model):
    coach = models.ForeignKey(Coach, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Full Name', null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date_of_birth = models.DateField(verbose_name='Date Of Birth', null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    list_gender = (
        ("male", "M"),
        ("female", "F"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=8, choices=list_gender, verbose_name='Gender')

    def  __str__(self):
	    return self.name

