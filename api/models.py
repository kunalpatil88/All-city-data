from django.db import models

class City(models.Model):
    
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)

