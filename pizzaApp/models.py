from django.db import models

# Create your models here.

class PizzaModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

class CustomerModel(models.Model):
    phone_no = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=10)

class OrderModel(models.Model):
    username = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    ordereditems = models.CharField(max_length=200)
    status = models.CharField(max_length=10, default="Pending")