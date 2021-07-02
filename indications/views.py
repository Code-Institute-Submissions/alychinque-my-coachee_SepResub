from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
#from .forms import *

class IndicationCreate(CreateView):
    model = Indication
    fields = ['title', 'description', 'category']
    success_url = "/"
    template_name = "indications/indication_create.html"

class IndicationList(ListView):
	model = Indication
	template_name = "indications/indication_list.html"
	context_object_name = 'indications'
	paginate_by = 10
	queryset = Indication.objects.all()