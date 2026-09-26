from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name