from django.db import models
from datetime import datetime,date

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dob = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True)
    insertdate = models.DateTimeField(auto_now_add=True,auto_now=False,)
    country = models.CharField(max_length=100)
    permanentadd = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    passwordnum = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    maritalstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Messege(models.Model):

    subject=models.CharField(max_length=100)
    messege=models.TextField()

    def __str__(self):
        return self.subject

class Friend(models.Model):
    email=models.EmailField()








