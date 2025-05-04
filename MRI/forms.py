from django import forms
from .models import MRI
from cliente.models import Cliente
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
        clientes = Cliente.objects.all()  
        for cliente in clientes:
            try:
                cliente.name = decrypt(cliente.name)
            except Exception as e:
                cliente.name = None
        self.fields['cliente'].queryset = clientes
