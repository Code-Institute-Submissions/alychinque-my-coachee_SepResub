from django.shortcuts import render

from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
#from .forms import *
from django.shortcuts import render, redirect, get_object_or_404, reverse

class CoachCreate(CreateView):
    model = Coach
    fields = [
        'name', 'date_of_birth', 'phone_number', 'gender'
    ]
    success_url = "/"
    template_name = "profiles/coach_create.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CoachCreate, self).form_valid(form)

class CoachList(ListView):
	model = Coach
	template_name = "profiles/coach_list.html"
	context_object_name = 'coaches'
	paginate_by = 10
	queryset = Coach.objects.all()

#view delete
#view update