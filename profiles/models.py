from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Full Name')
    date_of_birth = models.DateField(verbose_name='Date Of Birth')
    phone_number = models.CharField(max_length=20)
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
    coach = models.ForeignKey('Coach', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, verbose_name='Full Name')
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(verbose_name='Date Of Birth')
    phone_number = models.CharField(max_length=20)
    list_gender = (
        ("male", "M"),
        ("female", "F"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=8, choices=list_gender, verbose_name='Gender')
    list_indications = models.TextField(null=True, blank=True)

    def  __str__(self):
	    return self.name

