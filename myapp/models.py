from enum import unique
from pickle import TRUE
from unicodedata import name
from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length =100,unique=True)
    price = models.FloatField()
    description = models.CharField(max_length =200)
    