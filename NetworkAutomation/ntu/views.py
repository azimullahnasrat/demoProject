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
    ################

def add_switch(request):
    if request.method == 'POST':
        switch_form = CiscoSwitchForm(request.POST)
        if switch_form.is_valid():
            switch_form.save()
            return redirect('switch_list')  # Replace with your desired URL
        else:
            # Handle the second form submission
            username2 = request.POST.get('username2')
            email2 = request.POST.get('email2')
            password2 = request.POST.get('password2')
            # Implement your logic to create a new user
    else:
        switch_form = CiscoSwitchForm()

    return render(request, 'admin/form.html', {'form': switch_form})
##############
def switch_list(request):
    switches = CiscoSwitch.objects.all()
    return render(request, 'admin/list_sw.html', {'switches': switches})