from django.db import models

class Skill(models.Model):
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    mobile1=models.IntegerField()
    mobile2=models.IntegerField()
    nickname=models.CharField(max_length=45)
    facebook=models.CharField(max_length=45)
    whatsapp=models.CharField(max_length=45) 
    education=models.CharField(max_length=45) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

class Skill_cat(models.Model):
    categoty=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Education(models.Model):
    level=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Community(models.Model):
    community=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Evaluation(models.Model):
    evaluation_range=models.CharField(max_length=45)
    evaluation_comment=models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    city=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Governorate(models.Model):
    governorate=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)