import bcrypt
from django.shortcuts import render,redirect
from .models import *
from . import models
from django.contrib import messages


def login(request):
    
    return render(request,"login.html")

def regestration(request):
   
    return render(request,"regestration.html")

def login_worker(request):
    if request.method == 'POST':
        if request.POST['which_form'] == 'login':
            errors = Worker.objects.login_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/login')
            else:
                user = Worker.objects.get(email=request.POST['email']) 
                if user is not None:
                    # logged_user = user 
                    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                        request.session['user_name'] = user.first_name
                        return redirect('/enter')
                return redirect('/login')

        elif request.POST['which_form'] == 'register':
                errors = Worker.objects.reg_validator(request.POST)
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/regestration')
                else:
                #  if request.POST['which_form'] == 'register':
                    models.create_worker(request.POST)
                    return redirect('/login')
    return redirect('/login')

# def create_worker(request):
#     pass
