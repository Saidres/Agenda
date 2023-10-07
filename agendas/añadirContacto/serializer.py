from .models import contacto
from rest_framework import serializers

class contacto_serializer(serializers.ModelSerializer):
    class Meta:
        model = contacto
        fields = ['nombre', 'telefono', 'email']