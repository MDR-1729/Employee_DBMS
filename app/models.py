from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email_address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)