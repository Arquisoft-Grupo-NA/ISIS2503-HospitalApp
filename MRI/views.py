from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import MRIForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_MRI import create_mri, get_mris
from cliente.models import Cliente
from monitoring.crypto import decrypt
import logging

logger = logging.getLogger('django')

def MRI_list(request):
    mris = get_mris()
    paginator = Paginator(mris, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'MRI/MRI.html', {'page_obj': page_obj})

def MRI_create(request):
    clientes = Cliente.objects.all()  
    for cliente in clientes:
        try:
            cliente.name = decrypt(cliente.name) 
        except Exception as e:
            logger.error(f"Error al desencriptar el nombre del cliente: {str(e)}")

    if request.method == 'POST':
        form = MRIForm(request.POST)
        if form.is_valid():
            create_mri(form)
            messages.add_message(request, messages.SUCCESS, 'MRI creado exitosamente')
            return HttpResponseRedirect(reverse('MRICreate'))
        else:
            print(form.errors)
    else:
        form = MRIForm()

    context = {
        'form': form,
        'clientes': clientes,  
    }
    return render(request, 'MRI/MRICreate.html', context)
