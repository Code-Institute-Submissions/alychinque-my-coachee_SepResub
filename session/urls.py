from django.urls import path
from . import views
import session

app_name = 'session'

urlpatterns = [
    path('date/', views.session_date, name='session'),
    path('<int:coach>/', views.coach, name='coach'),
    path('agenda/', views.agenda, name='agenda-coach'),
    path('agenda-show/<int:id>/', views.agenda_show, name='agenda-show'),
    path('agenda-edit/<int:id>/', views.agenda_edit, name='agenda-edit'),
]
