from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'pages/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        return render(request, 'pages/contact.html', {'name': name})
    else:
        return render(request, 'pages/contact.html', {})

def about(request):
    return render(request, 'pages/about.html')

def pillars(request):
    return render(request, 'pages/pillars.html')

def plans(request):
    return render(request, 'pages/plans.html')

def coach_page(request):
    return render(request, 'pages/coach_page.html')
