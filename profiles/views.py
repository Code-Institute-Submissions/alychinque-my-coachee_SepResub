from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

class CoachCreate(CreateView):
    model = Coach
    fields = [
        'name', 'date_of_birth', 'phone_number', 'gender'
    ]
    success_url = "/coach_page/"
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


class CoacheeCreate(CreateView):
    model = Coachee
    fields = [
        'name', 'email', 'date_of_birth', 'phone_number', 'gender'
    ]
    success_url = "/"
    template_name = "profiles/coachee_create.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.coach = self.request.user.coach
        instance.save()
        return super(CoacheeCreate, self).form_valid(form)

class CoacheeList(ListView):
    model = Coachee
    template_name = "profiles/coachee_list.html"
    context_object_name = 'coachees'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super(CoacheeList, self).get_queryset()
        queryset = queryset.filter(coach=self.request.user.coach)
        return queryset

class CoacheeEdit(UpdateView):
	model = Coachee
	fields = ['name', 'email', 'date_of_birth', 'phone_number', 'gender']
	template_name = 'profiles/coachee_edit.html'
	success_url = '/profiles/coachee_list/'


class CoacheeDelete(DeleteView):
	model = Coachee
	template_name = 'profiles/coachee_delete.html'
	success_url = '/profiles/coachee_list/'
