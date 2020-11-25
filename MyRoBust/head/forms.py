from django import forms
from .models import *

class BusForm(forms.ModelForm):

      class Meta:
         model = Bus
         fields = ('busName','plateNumber', 'busFare')
         

