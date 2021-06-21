from home.views import index
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('plans', views.plans, name='plans'),
    path('pillars', views.pillars, name='pillars'),
]
