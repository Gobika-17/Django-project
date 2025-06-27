from django.db import models

# Create your models here.
class Car(models.Model):
    carname=models.CharField(max_length=255)
    price=models.FloatField()
    colour=models.CharField(max_length=255)
    image=models.CharField(max_length=2000)
 