from django.urls import path
from . import views

urlpatterns = [
    path('ntu/', views.ntu, name='ntu'),

]
