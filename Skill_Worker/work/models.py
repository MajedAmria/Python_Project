from tkinter import CASCADE
from django.db import models
from login.models import Worker

class Skill_cat(models.Model):
    categoty=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Education(models.Model):
    level=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Governorate(models.Model):
    governorate=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    city=models.CharField(max_length=45)
    governorate=models.ForeignKey(Governorate,related_name="cities",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Community(models.Model):
    community=models.CharField(max_length=45)
    governorate=models.ForeignKey(Governorate,related_name="communities",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    mobile1=models.IntegerField()
    mobile2=models.IntegerField()
    nickname=models.CharField(max_length=45)
    facebook=models.CharField(max_length=45)
    whatsapp=models.CharField(max_length=45) 
    worker=models.ForeignKey(Worker,related_name="skills",on_delete=models.CASCADE) 
    categoty=models.ForeignKey(Skill_cat,related_name="cats",on_delete=models.CASCADE)
    community=models.ForeignKey(Community,related_name="communities",on_delete=models.CASCADE)
    city=models.ForeignKey(City,related_name="cities",on_delete=models.CASCADE)
    education=models.ForeignKey(Education,related_name="educations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
class Evaluation(models.Model):
    evaluation_range=models.CharField(max_length=45)
    evaluation_comment=models.CharField(max_length=150)
    worker=models.ForeignKey(Worker,related_name="evaluations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
