from django.db import models

# Create your models here.

class CiscoSwitch(models.Model):
    ip_address = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

def switch_list(request):
    switches = CiscoSwitch.objects.all()
    return render(request, 'switch_list.html', {'switches': switches})

def add_switch(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        name = request.POST.get('name')
        password = request.POST.get('password')
        switch = CiscoSwitch.objects.create(ip_address=ip_address, name=name, password=password)