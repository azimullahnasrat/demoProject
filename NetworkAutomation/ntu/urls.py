from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from ntu.views import add_switch, switch_list

urlpatterns = [
    path('ntu/', views.ntu, name='ntu'),
    path('addswitch/', views.add_switch, name='addswitch'),
    path('switches/', views.switch_list, name='switches'),
    path('command/', views.command, name='command'),
    path('', views.cisco_command, name='cisco_command'),
    

]
