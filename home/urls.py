from home.views import index
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('plans/', views.plans, name='plans'),
    path('pillars/', views.pillars, name='pillars'),
    path('coach_page/', views.coach_page, name='coach_page'),
]
