from django import forms
from .models import *

class RegisterDriverForm(forms.ModelForm):
    
    class Meta:
        model = Driver
        fields = ('firstName', 'middleName', 'lastName', 'emailAddress', 'contactNumber', 'gender', 'busName', 'destination', 'plateNumber', 'seats', 'busFare', 'timeDeparture')