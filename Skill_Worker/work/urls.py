from django.urls import path
from . import views

urlpatterns = [
    path('dashbord',views.dashbord),
    path('login',views.return_to),
    path('rateworke',views.rate_work),
]