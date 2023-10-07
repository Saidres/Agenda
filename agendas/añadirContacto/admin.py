from django.contrib import admin
from .models import contacto

@admin.register(contacto)
class contactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email']
