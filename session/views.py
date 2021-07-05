from django.shortcuts import render
from .models import Session, Coachee
from .forms import AppointmentSessionForm


def session_create(request):
    template_name = 'session/session_create.html'

    if request.user.coach:
	    coach = request.user.coach
    else:
	    msg = 'You do not have permission.' 
	    context = {
			'msg':msg,
		}
	    return render(request, 'template_msg.html', context)

    coachees = Coachee.objects.filter(coach=coach)

    if not coachees:
	    msg = 'You do not have coachees.' 
	    context = {
			'msg':msg,
		}
	    return render(request, 'template_msg.html', context)

    if request.method == "POST":
        session_data = {
            'coach' : request.user.coach,
            'coachee_name' : request.POST.get('coachee_name'),
            'date' : request.POST.get('date'),
            'time' : request.POST.get('time'),
        }
        session_form = AppointmentSessionForm(session_data)
        if session_form.is_valid():
            session_form.save()
        coachee = Coachee.objects.get(name=request.POST.get('coachee_name'))
        if not Session.objects.filter(coach=coach, coachee=coachee).exists():
            session = 1
        else:
            session = Session.objects.filter(coach=coach, coachee=coachee).count() + 1
	    
    context = {
		'coachees':coachees,
    }

    return render(request, template_name, context)
