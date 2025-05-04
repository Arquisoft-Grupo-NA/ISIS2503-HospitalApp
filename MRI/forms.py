from django import forms
from .models import MRI
from cliente.logic.cliente_logic import get_clientes
from monitoring.crypto import decrypt

class MRIForm(forms.ModelForm):
    class Meta:
        model = MRI
        fields = ['cliente', 'fecha', 'hora', 'descripcion']
        labels = {
            'cliente': 'Cliente',
            'fecha': 'Fecha',
            'hora': 'Hora',
            'descripcion': 'Descripción'
        }

    def __init__(self, *args, **kwargs):
        super(MRIForm, self).__init__(*args, **kwargs)
        for cliente in self.fields['cliente'].queryset:
            try:
                cliente.name = decrypt(cliente.name)
                print(cliente.name)
                print("ola")
            except Exception as e:
                cliente.name = 'Desencriptación fallida'

        print(self.fields['cliente'].queryset)
        print("ola")