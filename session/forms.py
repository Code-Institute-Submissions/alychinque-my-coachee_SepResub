from django import forms
from .models import AppointmentSession, Session
from datetime import date


class SessionAppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentSession
        fields = ('coachee', 'date', 'time',)
        today = date.today()

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min':today}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        coachees = kwargs['coachees']
        kwargs.pop('coachees')
        super().__init__(*args, **kwargs)
        self.fields['coachee'].queryset=coachees


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('jornal', 'indications1', 'indications2', 'indications3', 'concluded')