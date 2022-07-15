from django.db import models

# Create your models here.



class Vehicle(models.Model):
    vehicleno = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    junction = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicleno