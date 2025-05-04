from django import forms
from .models import MRI
from cliente.models import Cliente

class MRIForm(forms.ModelForm):
    class Meta:
        model = MRI
        fields = ['cliente', 'fecha', 'hora', 'descripcion']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Selecciona un cliente")
