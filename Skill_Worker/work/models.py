
import bcrypt

from django.db import models
from login.models import Worker
import re

class SkillManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['address']) < 5:
            errors["address"] = "must be up than 5"
        if len(postData['mobile1']) < 10:
            errors["mobile1"] = "mobile number must be 10 or than"
        if len(postData['mobile2']) < 10:
            errors["mobile2"] = "mobile number must be 10 or than"
        if len(postData['facebook'])<5:
            errors['facebook']=" facebook name should be above 5"
        # today = datetime.now().strftime("%Y%m%d")
        # user_birthday = postData['birthdate'].replace("-", "")
        # if len(postData["birthdate"]) > 0 and datetime.strptime(postData["birthdate"], '%Y-%m-%d') >= datetime.today() :
        #     errors["birthdate"] = "Invalid Birth date"
        # if (int(today[0:4]) - int(user_birthday[0:4])) <= 18:
        #     errors["birthdate"] = "You should be at least 18 years old to register"
         
        return errors


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
    governorate=models.ForeignKey(Governorate,related_name="cities",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.city}"

class Community(models.Model):
    community=models.CharField(max_length=45)
    governorate=models.ForeignKey(Governorate,related_name="communities",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.community}"

class Skill(models.Model):
    address=models.CharField(max_length=100)
    phone=models.IntegerField(default=0)
    mobile1=models.IntegerField(default=0)
    mobile2=models.IntegerField(default=0)
    nickname=models.CharField(max_length=45, null = True, blank = True, default = "nickname")
    facebook=models.CharField(max_length=45)
    whatsapp=models.CharField(max_length=45) 
    worker=models.ForeignKey(Worker,related_name="skills",on_delete=models.CASCADE) 
    categoty=models.ForeignKey(Skill_cat,related_name="cats",on_delete=models.CASCADE)
    community=models.ForeignKey(Community,related_name="communities",on_delete=models.CASCADE)
    city=models.ForeignKey(City,related_name="cities",on_delete=models.CASCADE)
    education=models.ForeignKey(Education,related_name="educations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SkillManager()
    
    def __str__(self):
        return f"{self.address,self.phone,self.mobile1,self.mobile2,self.nickname,self.facebook,self.whatsapp,self.worker,self.categoty,self.community,self.city,self.education}"
   
class Evaluation(models.Model):
    evaluation_range=models.CharField(max_length=45)
    evaluation_comment=models.CharField(max_length=150)
    worker=models.ForeignKey(Worker,related_name="evaluations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.evaluation_comment,self.evaluation_range}"

def get_worker(info):
    return Worker.objects.get(id=info)

def get_skill(info):
    return Skill.objects.get(id=info)

def all_worker():
    return Worker.objects.all()

def all_skill():
    return Skill.objects.all()   

def all_governorate():
    return Governorate.objects.all()

def all_city():
    return City.objects.all()

def all_comm():
    return Community.objects.all()

def all_cat():
    return Skill_cat.objects.all() 

def all_edu():
    return Education.objects.all() 

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
    mobile1 = info['mobile1']
    mobile2= info['mobile2']
    address = info['address']
    facebook = info['facebook']
    category_id=Skill_cat.objects.get(id=info['category1'])
    community_id=Community.objects.get(id=info['village'])
    city_id=City.objects.get(id=info['city'])
    edu_id=Education.objects.get(id=info['education'])
    Skill.objects.create(address=address,mobile1=mobile1,mobile2=mobile2,facebook=facebook,
    worker=user_id,categoty=category_id,community=community_id,city=city_id,education=edu_id)

def update(info):
    password = info['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    x=Skill.objects.get(id=info)
    x.email=info['email']
    x.password=pw_hash
    x.mobile1=info['mobile1']
    x.mobile2=info['mobile2']
    x.address=info['address']
    x.save()

