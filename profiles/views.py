from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import CoachForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import stripe


@require_POST
def cache_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'date_of_birth': request.POST.get('date_of_birth'),
            'gender': request.POST.get('gender'),
            'username': request.user,
        })
        print('passou aqui')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def coach_create(request, plan, price):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if plan != 'Free':
        total = price
        stripe_total = round(int(total) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
    if request.method == "POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.plan = plan.capitalize()
            form.price = int(price)
            form.save()
            return redirect('coach_page')
        else:
            print('fail')
    else:

        form = CoachForm()
        order = {
            'plan': plan,
            'price': price,
        }
        if plan != 'Free':
            context = {
                'form': form,
                'order': order,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
        else:
            context = {
                'form': form,
                'order': order,
            }
        template_name = "profiles/coach_create.html"
        return render(request, template_name, context)


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
    success_url = "/coach_page/"
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
