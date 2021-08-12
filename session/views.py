from django.shortcuts import render
from .models import AppointmentSession, Coachee
from .forms import SessionForm


def session_date(request):
    coach = request.user.coach
    template_name = 'session/date.html'
    coachees = Coachee.objects.filter(coach=coach)
    if request.method == "GET":
        
        if not coachees:
            msg = 'You do not have coachees added.' 
            context = {
                'msg':msg,
            }
            return render(request, 'template_msg.html', context)

        form = SessionForm(coachees = coachees)
        context = {
            'form': form,
            'id': coach.id
        }
        
    
    if request.method == "POST":
        form = SessionForm(request.POST, coachees=coachees)
        
        if form.is_valid():
            coachee = request.POST.get('coachee')
            date = request.POST.get('date')
            sessionNumber = 1
            sessionInstance = AppointmentSession.objects.filter(coach=coach, coachee=coachee).order_by('-id').first()
            if sessionInstance:
                sessionNumber = sessionInstance.number_session + 1

            appointmentSession = AppointmentSession()
            appointmentSession.coach = coach
            appointmentSession.coachee = Coachee.objects.filter(id=coachee).first()
            appointmentSession.number_session = sessionNumber
            appointmentSession.date = date
            appointmentSession.time = request.POST.get('time')
            appointmentSession.save()

            template_name = 'pages/coach_page.html'
            context = {
                'coachee': coachee,
                'date': date,
                'msg': 'Appointment booked'
            }
        else:
            context = {
            'form': form,
            'id': coach.id
            }
    return render(request, template_name, context)

