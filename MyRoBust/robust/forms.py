from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from robust.models import Passenger,Admin, Driver, Bus, Booking, DashboardBus

class CreateUserForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['first_name','last_name','username','email','password1','password2']
            
class PassengerForm(forms.ModelForm):
    
        class Meta:
            model = Passenger
            fields = '__all__'

class BookingForm(forms.ModelForm):
        
        class Meta:
            model = Booking
            fields = ('seatNumber','dateReservation')
            
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
    
class DashboardBusForm(forms.ModelForm):

    class Meta:
        model = DashboardBus
        fields = ('totalBuses' ,)