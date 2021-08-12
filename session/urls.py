from django.urls import path
from . import views
import session

app_name = 'session'

urlpatterns = [
    path('date/', views.session_date, name='session'),
]
