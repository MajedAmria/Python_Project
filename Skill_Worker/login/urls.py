from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('regestration',views.regestration),
    path('loginworker',views.login_worker),
    # path('addskill',views.create_worker),
]