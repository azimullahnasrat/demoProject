from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from ntu.views import add_switch, switch_list

urlpatterns = [
    path('ntu/', views.ntu, name='ntu'),
    path('', add_switch, name='add_switch'),
    path('switches/', switch_list, name='switch_list'),

]
