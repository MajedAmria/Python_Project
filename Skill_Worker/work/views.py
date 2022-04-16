from django.shortcuts import render,redirect
from .models import *
from . import models
from django.contrib import messages

def dashbord(request):
    worker=models.all_worker()
    skill=models.all_skill()
    context={
        'this_worker':worker,
        'this_skill': skill,
    }
    return render(request,"dashbord.html",context)

def enter_to_skill(request):
   
    worker=models.all_worker()
    context={
     'worker':worker
     }
    return render(request,"rate.html",context)


def loguot(request):
    del request.session['email']
    return redirect('/dashbord')

def rate_work(request):
    return render(request,"ratework.html")