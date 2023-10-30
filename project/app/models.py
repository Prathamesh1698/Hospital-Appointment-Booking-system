from django.db import models
from datetime import datetime,date

class Medical(models.Model):
    CH1 = ((1,'Neurology'),(2,'Cardiology'),(3,'Eye care'),(4,'Pediatrics'))
    Patient_name =models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Mobile = models.BigIntegerField()
    Date = models.CharField( max_length=50)
    Department_name = models.IntegerField(choices=CH1)
    Doctor_name = models.CharField(max_length=50)
    uid = models.IntegerField()
    
    # def __str__(self):
        
    #     return self.Patient_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.BooleanField()