from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ClienteForm
from .logic.cliente_logic import get_clientes, create_cliente

def cliente_list(request):
    clientes = get_clientes()
    context = {
        'cliente_list': clientes
    }
    return render(request, 'cliente/clientes.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.success(request, 'Cliente creado exitosamente')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }
    return render(request, 'cliente/clienteCreate.html', context)
