from django.urls import path
from . import views

urlpatterns = [
    path('dashbord',views.dashbord),
    path('rateworke',views.rate_work),
    path('enter',views.enter_to_skill),
    path('logout',views.loguot),
  
]