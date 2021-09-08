from django.urls import path
from . import views
from .views import *


app_name = 'profiles'

urlpatterns = [
    path('coach_create/', views.coach_create, name='coach_create'),
    path('coach_list/', CoachList.as_view(), name='coach_list'),
    path('coachee_create/', CoacheeCreate.as_view(), name='coachee_create'),
    path('coachee_list/', CoacheeList.as_view(), name='coachee_list'),
    path('coachee_edit/<int:pk>/', CoacheeEdit.as_view(), name='coachee_edit'),
    path('coachee_delete/<int:pk>/', CoacheeDelete.as_view(), name='coachee_delete'),
]
