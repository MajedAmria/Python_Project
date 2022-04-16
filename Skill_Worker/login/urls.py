from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('regestration',views.regestration),
    path('reg',views.reg),
    path('addskill',views.create_worker),
]