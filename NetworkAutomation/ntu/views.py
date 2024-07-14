import sys
from getpass import getpass
from netmiko import ConnectHandler
from django.shortcuts import render
from netmiko.snmp_autodetect import SNMPDetect
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
            return redirect('switches')  # Replace with your desired URL
        else:
            # Handle the second form submission
            ip_address = request.POST.get('ip_address')
            name = request.POST.get('name')
            password = request.POST.get('password')
            # Implement your logic to create a new user
    else:
        switch_form = CiscoSwitchForm()

    return render(request, 'admin/form.html', {'form': switch_form})


def switch_list(request):
    switches = CiscoSwitch.objects.all()
    switch_data = []

    for switch in switches:
        host = switch.ip_address  # Get the IP address from the CiscoSwitch model
        password=switch.password
        device = {
            "host": host,
            "username": "root",
            "password": password
        }

        snmp_community = "mew"
        my_snmp = SNMPDetect(
            host, snmp_version="v2c", community=snmp_community
        )
        device_type = my_snmp.autodetect()

        if device_type is None:
            sys.exit("SNMP failed!")

        device["device_type"] = device_type
        with ConnectHandler(**device) as net_connect:
            switch_data.append({
                "ip_address": switch.ip_address,
                "device_type": device_type
            })

    return render(request, 'admin/list_sw.html', {'switches': switch_data})