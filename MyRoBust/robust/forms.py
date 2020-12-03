from django import forms
from .models import *


class PassengerForm(forms.ModelForm):
    
        class Meta:
            model = Passenger
            fields = '__all__'

class BookingForm(forms.ModelForm):
        
        class Meta:
            model = Booking
            fields = ('seatNumber',)
            
class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('busName','plateNumber', 'busFare')

class RegisterDriverForm(forms.ModelForm):
    
    class Meta:
        model = Driver
        fields = ('profilePicture', 'firstName', 'lastName', 'emailAddress', 'contactNumber', 'gender')
         

class AdministratorForm(forms.ModelForm):
    
    class Meta:
        model = Admin
        fields = ('firstName', 'middleName', 'lastName', 'emailAddress', 'contactNumber', 'username', 'password')
         