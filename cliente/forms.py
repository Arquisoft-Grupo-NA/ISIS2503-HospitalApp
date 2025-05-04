from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'info_personal']
        labels = {
            'name': 'Nombre',
            'info_personal': 'Información Personal'
        }
