import re

from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from .models import Vehicle


class VehicleForm(ModelForm):
    """
    Create Vehicle parking form
    """
    registration_number = forms.CharField(max_length=13, required=True)
    color = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Vehicle
        fields = ('registration_number', 'color')

    def clean_registration_number(self):
        registration_number = self.cleaned_data['registration_number']

        regex = r"^[A-Z]{2}[-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}$"

        if not re.match(regex, registration_number):
            raise forms.ValidationError('Enter Valid Registration Number in given format:- {}'.format('KA-04-TY-3469'))
        return registration_number
