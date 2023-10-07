from django.urls import path
from  .views import contactoView
urlpatterns = [
    path('listar', contactoView.as_view(), name='listar-contacto'),
    path('guardar', contactoView.as_view(), name='guardar-contacto'),
    path('editar', contactoView.as_view(), name='editar-contacto'),


]