from django import forms
from .models import MRI
from cliente.logic.logic_cliente import get_clientes
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
        clientes = get_clientes()
        self.fields['cliente'].queryset = clientes
