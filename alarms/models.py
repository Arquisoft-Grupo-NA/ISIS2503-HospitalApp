from django.db import models
from cliente.models import cliente
from MRI.models import MRI

class Alarm(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, default=None)
    MRI = models.ForeignKey(MRI, on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"cliente": %s, "MRI": %s, "fecha": %s, "dateTime": %s}' % (self.cliente.name, self.MRI.descripcion, self.MRI.fecha, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'cliente': self.cliente.name,
            'MRI': self.MRI.descripcion,
            'fecha': self.MRI.fecha,
            'dateTime': self.dateTime,
          
        }
        return alarm