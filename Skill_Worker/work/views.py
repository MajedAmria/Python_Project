from django.shortcuts import render,redirect


def dashbord(request):
    return render(request,"dashbord.html")

def returnto():
    return redirect('/login')