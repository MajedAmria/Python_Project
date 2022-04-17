import datetime
import bcrypt
from django.db import models
from birthday import BirthdayField, BirthdayManager
import re

class WorkManager(models.Manager):
    def login_validator(self,postData):
        user = Worker.objects.filter(email=postData['email']) 
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if not len(user):
            errors['email']="email is not valid"
        if len(postData['password']) < 8:
            errors['password'] = "Blog password should be at least 8 characters"
        if len(user) and not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors["password"] = "Wrong Password! / Password doesn't match!"
        else:
            print("password Match")
        return errors

    def reg_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Blog first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Blog last name should be at least 3 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        new_user_email=Worker.objects.filter(email=postData['email'])
        if len(new_user_email):
            errors['email']="email is already exsist"
        if len(postData['password']) < 8:
            errors["password"] = "Blog password should be at least 8 characters" 
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Not confirm password" 
        # today = datetime.now().strftime("%Y%m%d")
        # user_birthday = postData['birthdate'].replace("-", "")
        # if len(postData["birthdate"]) > 0 and datetime.strptime(postData["birthdate"], '%Y-%m-%d') >= datetime.today() :
        #     errors["birthdate"] = "Invalid Birth date"
        # if (int(today[0:4]) - int(user_birthday[0:4])) <= 18:
        #     errors["birthdate"] = "You should be at least 18 years old to register"
         
        return errors



class Worker(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    password=models.CharField(max_length=10)
    birthdate=BirthdayField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects1 = BirthdayManager()
    objects = WorkManager()
    def __str__(self):
        return f"{self.first_name,self.last_name}"

def create_worker(info):
    password = info['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
    print(pw_hash)
    Worker.objects.create(first_name=info['first_name'],last_name=info['last_name'],email=info['email'],password=pw_hash,birthdate=convert_str_date(info['birthdate']))

def convert_str_date(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d').date()
