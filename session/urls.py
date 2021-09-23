from django.urls import path
from . import views
import session

app_name = 'session'

urlpatterns = [
    path('date/', views.session_date, name='session_date'),
    path('<int:coach>/', views.coach, name='coach'),
    path('agenda/', views.agenda, name='agenda_coach'),
    path('agenda_show/<int:id>/', views.agenda_show, name='agenda_show'),
    path('date_edit/<int:id>/', views.session_edit, name='date_edit'),
    path('date_delete/<int:id>/', views.session_delete, name='date_delete'),
]
