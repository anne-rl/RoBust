from django.db import models

# Create your models here.
class Passenger(models.Model):
        passengerID = models.CharField(max_length = 100, primary_key = True)
        firstName = models.CharField(max_length = 100)
        middleName = models.CharField(max_length = 100)
        lastName = models.CharField(max_length = 100)
        emailAddress = models.EmailField()
        contactNumber = models.CharField(max_length = 100)
        department = models.CharField(max_length = 100)
        gender = models.CharField(max_length = 100)
        password = models.CharField(max_length = 15)

        class Meta:
            db_table = "Passenger"

class Bus(models.Model):
        busNumber = models.AutoField(primary_key=True)
        busName = models.CharField(max_length = 50)
        plateNumber = models.CharField(max_length = 50)
        destination = models.CharField(max_length = 50)
        totalSeats = models.IntegerField()
        busFare = models.FloatField()
        departureTime = models.TimeField()
        #driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='bus_driver')
    
        class Meta:
            db_table = "Bus"

