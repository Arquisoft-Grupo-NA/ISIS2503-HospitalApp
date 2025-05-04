from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import MRIForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_MRI import get_mris
from cliente.logic.cliente_logic import get_clientes
from monitoring.crypto import decrypt
import logging
from MRI.logic.logic_MRI import create_mri

logger = logging.getLogger('django')

def MRI_list(request):
    mris = get_mris()

    for mri in mris:
        mri.cliente.name = decrypt(mri.cliente.name)

    paginator = Paginator(mris, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'MRI/MRI.html', {'page_obj': page_obj})

def MRI_create(request):
    if request.method == 'POST':
        form = MRIForm(request.POST)
        if form.is_valid():
            form.save()
            create_mri(form)
    else:
        form = MRIForm()
    

    clientes = get_clientes()
    
    context = {
        'form': form,
        'clientes': clientes,
    }
    return render(request, 'MRI/MRICreate.html', context)