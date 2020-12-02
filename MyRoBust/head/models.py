from django.db import models
from user.models import *
from django.utils import timezone

class Bus(models.Model):
        busName = models.CharField(max_length = 50)
        plateNumber = models.CharField(max_length = 50)
        destination = models.CharField(max_length = 50)
        totalSeats = models.PositiveSmallIntegerField(default=0)
        busFare = models.PositiveSmallIntegerField(default=0)
        departureTime = models.TimeField(default = timezone.now)
        img = models.FileField(upload_to='media', null = True)
        #driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='bus_driver')
    
        class Meta:
            db_table = "Bus"

class Driver(models.Model):
        profilePicture = models.ImageField(upload_to='images/', null=True, blank=True)
        firstName = models.CharField(max_length = 50)
        middleName = models.CharField(max_length = 50)
        lastName = models.CharField(max_length = 50)
        emailAddress = models.CharField(max_length = 50)
        contactNumber = models.CharField(max_length = 50)
        gender = models.CharField(max_length = 20)

        class Meta:
            db_table = "Driver"

class Admin(models.Model):
        username = models.CharField(max_length = 50, primary_key = True)
        password = models.CharField(max_length = 50)
        firstName = models.CharField(max_length = 50)
        middleName = models.CharField(max_length = 50)
        lastName = models.CharField(max_length = 50)
        emailAddress = models.CharField(max_length = 50)
        contactNumber = models.IntegerField()
        username = models.CharField(max_length = 50, primary_key = True)
        password = models.CharField(max_length = 50)

        class Meta:
            db_table = "Admin"



