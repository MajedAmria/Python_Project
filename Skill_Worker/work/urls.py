from django.urls import path
from . import views

urlpatterns = [
    path('dashbord',views.dashbord),
    path('rateworke',views.rate_work),
    path('enter',views.enter_to_skill),
    path('update',views.update_skill),
    path('show/<int:worker_id>',views.show_worker),
    path('add',views.add_skill),
    path('addto',views.add_to_skill),
    path('updateskill/<int:id>',views.update),
    path('logout',views.loguot),
  
]