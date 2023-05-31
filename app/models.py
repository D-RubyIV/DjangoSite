from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    mail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    idProduct = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Oder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    oderDate = models.DateTimeField(auto_now_add=True)
    nameProduct = models.CharField(max_length=200, null=True)
    countOder = models.IntegerField()
    status = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.status
    
class ItemOder(models.Model):
    oder = models.ForeignKey(Oder, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField()
    oderDate = models.DateTimeField(auto_now_add=True)