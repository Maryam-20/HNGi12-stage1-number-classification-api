from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
class NumberProperty(models.Model):
    number = models.BigIntegerField(primary_key=True)
    is_prime = models.BooleanField(default=False)
    is_perfect = models.BooleanField(default=False)
   
