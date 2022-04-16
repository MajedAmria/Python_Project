from django.db import models
from birthday import BirthdayField, BirthdayManager


class Worker(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    password=models.CharField(max_length=10)
    birthdate=BirthdayField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BirthdayManager()
