from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=120)
    name_hmac = models.CharField(max_length=64, blank=True)
    info_personal = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)

