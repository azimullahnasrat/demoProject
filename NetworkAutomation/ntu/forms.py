from django import forms
from .models import CiscoSwitch

class CiscoSwitchForm(forms.ModelForm):
    class Meta:
        model = CiscoSwitch
        fields = ['ip_address', 'name', 'password']
class CiscoCommandForm(forms.Form):
    command = forms.CharField(label='Cisco Command', widget=forms.TextInput(attrs={'class': 'form-control'}))