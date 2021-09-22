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
	ordering = ['id']

class IndicationEdit(UpdateView):
	model = Indication
	fields = ['title', 'description', 'category']
	template_name = 'indications/indication_edit.html'
	success_url = '/indications/indication_list/'


class IndicationDelete(DeleteView):
	model = Indication
	template_name = 'indications/indication_delete.html'
	success_url = '/indications/indication_list/'