from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    name = models.CharField(max_length=50, verbose_name='Full Name')
    birthday = models.CharField(max_length=11, verbose_name='Birthday')
    phone = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    list_gender = (
        ("male", "M"),
        ("female", "F"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=8, choices=list_gender, verbose_name='Gender')
