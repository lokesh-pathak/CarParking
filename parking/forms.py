from django import forms
from django.forms import ModelForm

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
