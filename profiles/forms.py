from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput
from .models import Coach
from datetime import date


class CoachForm(forms.ModelForm):
    
    
    class Meta:
        model = Coach
        fields = ('name', 'date_of_birth', 'phone_number', 'gender', 'plan')

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'date_of_birth': 'Date Of Birth',
            'phone_number': 'Phone Number',
            'gender': 'Gender',
            'plan': 'Plan',
            
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = field

        