from distutils.command.upload import upload
from email.mime import image
from enum import unique
from pickle import TRUE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length =100,unique=True)
    price = models.FloatField()
    description = models.CharField(max_length =200)
    image=models.ImageField(blank=True,upload_to='images')
    seller_name = models.ForeignKey(User,on_delete=models.CASCADE,default=2)



#addtocart
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price