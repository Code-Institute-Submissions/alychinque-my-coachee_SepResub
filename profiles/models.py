from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    list_plans = {
        ('Premium', 'Premium'),
        ('Standard', 'Standard'),
        ('Basic', 'Basic'),
        ('Free', 'Free')
    }
    plan = models.CharField(max_length=10, null=False, blank=False, choices=list_plans)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    stripe_pid = models.CharField(max_length=254, null=True, blank=False, default='')

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

