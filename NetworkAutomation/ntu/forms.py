from django import forms
from .models import CiscoSwitch

class CiscoSwitchForm(forms.ModelForm):
    class Meta:
        model = CiscoSwitch
        fields = ['ip_address', 'name', 'password']