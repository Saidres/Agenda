import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import contacto
from .serializer import contacto_serializer

# Create your views here.

class contactoView(APIView):
    def get(self, request, *args, **kwargs):
        lista_contacto = contacto.objects.all()
        serializer_contacto = contacto_serializer(lista_contacto, many=True)
        return Response(serializer_contacto.data, status= status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono'),
            'email': request.data.get('email'),      
        }
        serializador = contacto_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
        
    