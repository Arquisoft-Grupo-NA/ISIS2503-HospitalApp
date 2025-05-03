from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    name_hmac = models.CharField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)

