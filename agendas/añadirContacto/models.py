from django.db import models

# Create your models here.
class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    
