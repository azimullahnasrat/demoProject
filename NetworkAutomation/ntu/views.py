import sys
from getpass import getpass
from netmiko import ConnectHandler
import subprocess
import netmiko
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from .forms import CiscoSwitchForm
from .models import CiscoSwitch
from .forms import CiscoCommandForm
import time

def ntu(request):
    var={'name':"azimullah"}
    return render(request,'admin/index.html',context=var)

def add_switch(request):
    if request.method == 'POST':
        switch_form = CiscoSwitchForm(request.POST)
        if switch_form.is_valid():
            switch_form.save()
            return redirect('switches')
        else:
            # Handle the second form submission
            ip_address = request.POST.get('ip_address')
            name = request.POST.get('name')
            password = request.POST.get('password')
            # Implement your logic to create a new user
    else:
        switch_form = CiscoSwitchForm()

    return render(request, 'admin/form.html', {'form': switch_form})

def ping_device(host):
    try:
        subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def switch_list(request):
    switches = CiscoSwitch.objects.all()
    online_switches = []
    offline_switches = []
    for switch in switches:
        if ping_device(switch.ip_address):
            online_switches.append(switch)
        else:
            offline_switches.append(switch)
    return render(request, 'admin/list_sw.html', {'online_switches': online_switches, 'offline_switches': offline_switches})

def command(request):
    
    return render(request,'admin/command.html')

def cisco_command(request):
    if request.method == 'POST':
        form = CiscoCommandForm(request.POST)
        if form.is_valid():
            ip_address = request.POST.get('ip_address')
            command = request.POST.get('command')
            password = "Admin@sw.mew.gov.af2022"

            try:
                # Cisco device connection details
                device = {
                    'device_type': 'cisco_ios',
                    'host': ip_address,
                    'username': "root",
                    'password': password,
                    'secret': password,
                }

                # Connect to the Cisco device and execute the command
                connection = ConnectHandler(**device)
                time.sleep(1)
                connection.enable()  # Go to enable mode
                time.sleep(1)  # Wait for 1 seconds in enable mode
                connection.send_command("enable")
                time.sleep(1)  # Wait for 1 seconds after entering enable mode
                connection.send_command(password)
                time.sleep(1)  # Wait for 1 seconds after entering enable mode
                output = connection.send_command(command)
                connection.disconnect()
                return render(request, 'admin/command.html', {'output': output})
            except Exception as e:
                return render(request, 'admin/command.html', {'error': str(e)})
    else:
        form = CiscoCommandForm()
    return render(request, 'admin/command.html', {'form': form})