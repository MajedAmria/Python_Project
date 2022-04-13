from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('reg',views.regestration),
    path('reg',views.reg)
]