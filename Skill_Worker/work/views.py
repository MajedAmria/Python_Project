from django.shortcuts import render,redirect
from .models import *
from . import models
from django.contrib import messages

def dashbord(request):
    worker=models.all_worker()
    skill=models.all_skill()
    governorate=models.all_governorate()
    city=models.all_city()
    comm=models.all_comm()
    category=models.all_cat()
    context={
        'all_workers':worker,
        'this_skill': skill,
        'this_governorate':governorate,
        'this_city':city,
        'this_comminty':comm,
        'this_category':category,
    }
    return render(request,"dashbord.html",context)

def add_skill(request):
    governorate=models.all_governorate()
    city=models.all_city()
    comm=models.all_comm()
    cat=models.all_cat()
    edu=models.all_edu()
    context={
        'this_governorate':governorate,
        'this_city':city,
        'this_comminty':comm,
        'this_category':cat,
        'this_edu': edu,
        'user_name':  request.session['user_name'],
    }
    return render(request,"addskill.html",context)

def add_to_skill(request):
    if request.method == 'POST':
        errors = Skill.objects.reg_validator(request.POST)
        if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/add')
        else:    
           print("**********",request.POST)        
           models.create_skill(request.POST)

           return redirect('/enter')

def update_skill(request):
    governorate=models.all_governorate()
    city=models.all_city()
    comm=models.all_comm()
    cat=models.all_cat()
    edu=models.all_edu()
    context={
        'this_governorate':governorate,
        'this_city':city,
        'this_comminty':comm,
        'this_category':cat,
        'this_edu': edu,
        'email':  request.session['email'],
    }
    return render(request,"Updateskillprof.html",context)

def update(request,id):
    if request.method == 'POST':
        errors = Skill.objects.update_validator(request.POST)
        if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/login')
        else:
            models.update(request.POST)
            return redirect('/enter')
    return redirect('/enter')

def show_worker(request,worker_id):
    worker=models.get_worker(worker_id)
    context={
        'this_worker':worker,
    }
        
    return render(request,"view.html",context)

def enter_to_skill(request):
    worker=models.all_worker()
    context={
     'worker':worker,
     'logged_user' : request.session['user_name'],
     }
    return render(request,"rate.html",context)


def loguot(request):
    del request.session['user_name']
    return redirect('/dashbord')

def rate_work(request):
    return render(request,"ratework.html")