from MRI.models import MRI
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_mri_by_cliente(cliente):
    queryset = MRI.objects.filter(name=cliente).order_by('-dateTime')[:10]
    return (queryset)
s
def create_alarm(cliente, mri, limitExceeded):
    alarm = Alarm()
    alarm.cliente = cliente
    alarm.MRI = MRI
    alarm.fecha = mri.fecha
    alarm.save()
    return alarm