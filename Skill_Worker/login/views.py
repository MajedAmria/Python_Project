from django.shortcuts import render,redirect
from .models import *
from . import models
from django.contrib import messages

def login(request):
    
    return render(request,"login.html")

def regestration(request):
   
    return render(request,"regestration.html")

def reg(request):
    errors = Worker.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/reg')
    return redirect('/login')

def create_worker(request):
    print("****",request.POST)
    # print("00000000000",type(request.POST['birthdate']))
    models.create_worker(request.POST)
    
    return redirect('/login')
