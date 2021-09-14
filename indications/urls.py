from django.urls import path
from .views import *


app_name = 'indications'

urlpatterns = [
    path('create/', IndicationCreate.as_view(), name='create'),
    path('list/',IndicationList.as_view(), name='list'),
    path('indication_edit/<int:pk>/', IndicationEdit.as_view(), name='indication_edit'),
    path('indication_delete/<int:pk>/', IndicationDelete.as_view(), name='indication_delete'),
]