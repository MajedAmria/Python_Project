from django.shortcuts import render,redirect


def dashbord(request):
    return render(request,"dashbord.html")

def return_to():
    return redirect('/login')

def rate_work(request):
    return render(request,"ratework.html")