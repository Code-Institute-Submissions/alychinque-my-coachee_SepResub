from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        #send an email
        send_mail(
            'New message from ' + name, #subject
            message, #message
            email, #from email
            ['alychinque@gmail.com'], #to email
        )
        return render(request, 'home/contact.html', {'name': name})
    else:
        return render(request, 'home/contact.html', {})

def about(request):
    return render(request, 'home/about.html')

def pillars(request):
    return render(request, 'home/pillars.html')

def plans(request):
    return render(request, 'home/plans.html')
