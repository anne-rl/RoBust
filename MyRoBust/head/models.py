from django.db import models
from user.models import *

class Bus(models.Model):
        busName = models.CharField(max_length = 50)
        plateNumber = models.CharField(max_length = 50)
        destination = models.CharField(max_length = 50)
        totalSeats = models.IntegerField()
        busFare = models.FloatField()
        departureTime = models.TimeField()
        img = models.FileField(upload_to='media', null = True)
        #driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='bus_driver')
    
        class Meta:
            db_table = "Bus"

class Driver(models.Model):
        firstName = models.CharField(max_length = 50)
        middleName = models.CharField(max_length = 50)
        lastName = models.CharField(max_length = 50)
        emailAddress = models.CharField(max_length = 50)
        contactNumber = models.CharField(max_length = 50)
        gender = models.CharField(max_length = 20)

        class Meta:
            db_table = "Driver"


