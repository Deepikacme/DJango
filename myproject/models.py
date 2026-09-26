from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.IntegerField()

   