from django import forms
from .models import *

class BusForm(forms.ModelForm):

      class Meta:
        model = Bus
        fields = ('busName','plateNumber', 'busFare')

class RegisterDriverForm(forms.ModelForm):
    
    class Meta:
        model = Driver
        fields = ('firstName', 'middleName', 'lastName', 'emailAddress', 'contactNumber', 'gender')
         

