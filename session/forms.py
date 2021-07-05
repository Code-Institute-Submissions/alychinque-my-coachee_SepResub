from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import AppointmentSession


class AppointmentSessionForm(forms.ModelForm):
    class Meta:
        model = AppointmentSession
        fields = ('coachee', 'session', 'date', 'time')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'coachee_name': 'Coachee Name',
            'session': 'Number of Session',
            'date': 'Date of the session',
        }
        widgets = {
            'date': DateInput(format='%d-%m-%Y'),
            'time': TimeInput(),
        }

        self.fields['coachee'].widget.attrs['autofocus'] = True