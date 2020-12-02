from django.db import models
from head.models import *

# Create your models here.
class Passenger(models.Model):
    username = models.CharField(max_length = 100, primary_key = True)
    firstName = models.CharField(max_length = 100)
    middleName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    emailAddress = models.EmailField()
    contactNumber = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    password = models.CharField(max_length = 15)
    availableBalance = models.IntegerField()
    currentCashIn = models.IntegerField()

    class Meta:
        db_table = "Passenger"
    
class Booking(Bus):
    BusID = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='bookingBusID', null=True, blank = True)
    seatNumber = models.CharField(max_length = 15)
    
    class Meta:
        db_table = "Booking"