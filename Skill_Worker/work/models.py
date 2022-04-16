from tkinter import CASCADE

from django.db import models
from login.models import Worker
import re




class Skill_cat(models.Model):
    categoty=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.categoty}"

class Education(models.Model):
    level=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.level}"

class Governorate(models.Model):
    governorate=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.governorate}"

class City(models.Model):
    city=models.CharField(max_length=45)
    governorate=models.ForeignKey(Governorate,related_name="cities",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.city}"

class Community(models.Model):
    community=models.CharField(max_length=45)
    governorate=models.ForeignKey(Governorate,related_name="communities",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.community}"

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
    def __str__(self):
        return f"{self.evaluation_comment,self.evaluation_range}"

def all_worker():
    return Worker.objects.all()

def all_skill():
    return Skill.objects.all()   

def create_categoty(info):
    Skill_cat.objects.create(categoty=info['categoty'])

def create_comm(info):
    governorate_id=Governorate.objects.get(id=info['id'])
    Community.objects.create(community=info['community'],governorate=governorate_id)

def create_city(info):
    governorate_id=Governorate.objects.get(id=info['id'])
    City.objects.create(city=info['city'],governorate=governorate_id)

def create_edu(info):
    Education.objects.create(level=info['level'])

def create_governorate(info):
    Governorate.objects.create(governorate=info['governorate'])

def create_evaluation(info):
    Evaluation.objects.create(evaluation_range=info['evaluation_range'],evaluation_comment=info['evaluation_comment'])

def create_skill(info):
    user=info['worker']
    user_id=Worker.objects.get(id=user)
    category_id=Skill_cat.objects.get(id=info['id'])
    community_id=Community.objects.get(id=info['id'])
    city_id=City.objects.get(id=info['id'])
    edu_id=Education.objects.get(id=info['id'])
    Skill.objects.create(address=info['address'],phone=info['phone'],mobile1=info['mobile1'],
    mobile2=info['mobile2'],nickname=info['nickname'],facebook=info['facebook'],
    whatsapp=info['whatsapp'],worker=user_id,category=category_id,community=community_id,city=city_id,education=edu_id)
