from django.urls import path
from . import views

urlpatterns = [
    path('dashbord',views.dashbord),
    path('login',views.returnto)
]