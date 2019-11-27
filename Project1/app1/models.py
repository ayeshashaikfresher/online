from django.db import models

class AdminModel(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)

class MerchantModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=40)

class Product(models.Model):
    pro_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price =models.FloatField()
    quantity = models.IntegerField(10)


class CustomerModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contactno = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=8)
    status = models.CharField(max_length=10)