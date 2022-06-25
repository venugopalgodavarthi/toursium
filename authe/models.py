from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registermodel(User):
    age=models.PositiveIntegerField()
    phone=models.PositiveBigIntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=10,choices=[['MALE','MALE'],['FEMALE','FEMALE'],['others','others']])
    