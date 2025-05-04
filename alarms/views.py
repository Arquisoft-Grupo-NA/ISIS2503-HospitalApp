from django.http import JsonResponse
from django.shortcuts import render

from cliente.logic.cliente_logic import get_cliente_by_id
from .logic.logic_alarm import get_alarms, get_mri_by_cliente, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, variable_id):
    cliente = get_cliente_by_id(variable_id)
    mris = get_mri_by_cliente(variable_id)
    createAlarm = False
    upperMeasurement = None
    current_date = timezone.now().date()
    for mri in mris:
    
        if mri.fecha <= current_date:
            createAlarm = True
            upperMeasurement = mri
            
            
    # Si la alarma debe ser creada
    if createAlarm:
        alarm = create_alarm(cliente, upperMeasurement, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)

