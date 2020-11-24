from django.db import models

class Driver(models.Model):
    firstName = models.CharField(max_length = 50)
    middleName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    emailAddress = models.CharField(max_length = 50)
    contactNumber = models.IntegerField()
    gender = models.CharField(max_length = 20)
    busName = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    plateNumber = models.CharField(max_length = 50)
    seats = models.CharField(max_length = 20)
    busFare = models.CharField(max_length = 20)
    timeDeparture = models.CharField(max_length = 20)
    
    class Meta:
        db_table = "Driver"