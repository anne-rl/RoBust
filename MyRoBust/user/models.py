from django.db import models
from head.models import Bus

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
