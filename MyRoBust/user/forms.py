from django import forms
from .models import *
from head.forms import *

class PassengerForm(forms.ModelForm):
    
        class Meta:
            model = Passenger
            fields = '__all__'

#class BookingForm(forms.ModelForm):
#        
#        class Meta:
#            model = Booking
#            fields = '__all__'