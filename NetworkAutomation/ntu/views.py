from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from netmiko import ConnectHandler
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from .forms import CiscoSwitchForm
from .models import CiscoSwitch
def ntu(request):

    var={'name':"azimullah"}
    return render(request,'admin/index.html',context=var)

def add_switch(request):
    if request.method == 'POST':
        form = CiscoSwitchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('switch_list')
    else:
        form = CiscoSwitchForm()
    return render(request, 'admin/form.html', {'form': form})

def switch_list(request):
    switches = CiscoSwitch.objects.all()
    return render(request, 'admin/list_sw.html', {'switches': switches})