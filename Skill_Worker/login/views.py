from django.shortcuts import render,redirect

def login(request):
    return render(request,"login.html")

def regestration(request):
    return render(request,"regestration.html")

def reg():
    return redirect('/reg')