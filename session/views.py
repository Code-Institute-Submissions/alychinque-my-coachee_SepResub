from django.shortcuts import render
from .models import AppointmentSession, Coachee, Session
from .forms import SessionForm
from django.http.response import HttpResponse
import json


def session_date(request):
    coach = request.user.coach
    template_name = 'session/date.html'
    coachees = Coachee.objects.filter(coach=coach)
    if request.method == "GET":
        
       

        form = SessionForm(coachees = coachees)
        context = {
            'coachee': '',
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


def coach(request, coach):
    agenda = AppointmentSession.objects.filter(coach=coach, date=request.GET.get('date', None)).order_by('time')
    agenda = [{
        'id': a.id,
        'coachee': a.coachee.name,
        'number_session': a.number_session,
        'date': a.date.strftime('%d/%m/%Y'),
        'time': a.time.strftime('%H:%M'),
    } for a in agenda]
    jsondict = json.dumps({'agenda': agenda})
    return HttpResponse(jsondict, content_type='application/json')


def agenda(request):
    coach = request.user.coach
    agenda = AppointmentSession.objects.filter(coach=coach).order_by('date', 'time')
    return render(request, 'session/agenda.html', context= { 'agenda': agenda })


def agenda_show(request, id):
    session_sessao = Session.objects.filter(appointment_session__id=id)
    return render(request, 'session/agenda_show.html', context={ 'session': session_sessao})


def agenda_edit(request, id):
    
    return render(request, 'session/agenda_edit.html', context={})


def session_edit(request, id):
    """
    Edits the session 
    """
    coach = request.user.coach
    coachees = Coachee.objects.filter(coach=coach)
    agenda = AppointmentSession.objects.filter(id=id)
    for a in agenda:
        agenda2 = {
            'coachee': (a.coachee.name),
            'number_session': (a.number_session),
            'date': (a.date),
            'time': (a.time),
        }
    
    form = SessionForm(coachees = coachees)
    template_name = 'session/date_edit.html'
    context = {
        'form': form,
        'id': coach.id,
        'agenda': agenda
    }

    if request.method == "POST":
        form = SessionForm(request.POST, coachees=coachees)
        agenda.delete()
        if form.is_valid():
            coachee = request.POST.get('coachee')
            date = request.POST.get('date')
            sessionNumber = agenda2['number_session']
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

def session_delete(request, id):
    """
    Deletes the session
    """
    agenda_delete = AppointmentSession.objects.filter(id=id)
    agenda_delete.delete()
    template_name = 'session/agenda.html'
    coach = request.user.coach
    agenda = AppointmentSession.objects.filter(coach=coach).order_by('date', 'time')

    return render(request, template_name, context= { 'agenda': agenda })
    