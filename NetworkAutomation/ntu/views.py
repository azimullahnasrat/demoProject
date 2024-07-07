from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from netmiko import ConnectHandler
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
def ntu(request):

    var={'name':"azimullah"}
    return render(request,'admin/index.html',context=var)

