from django.urls import path
from .views import *

urlpatterns = [
    path('coach_create', CoachCreate.as_view(), name='coach_create'),
    path('coach_list', CoachList.as_view(), name='coach_list'),
]
