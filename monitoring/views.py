from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

import logging

logger = logging.getLogger('django')

def index(request):
    return render(request, 'index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

def mi_vista_de_prueba(request):
    logger.info("Accediendo a la vista de prueba de error desde monitoring/views.py")
    raise ValueError("Este es un error de prueba intencional desde monitoring/views.py.")
    return HttpResponse("OK")

def logout_view(request):
    logout(request) 
    return redirect('/')  
