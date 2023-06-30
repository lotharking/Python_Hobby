from django.urls import path
from .views import crear_cliente, listar_cliente

app_name = 'clientes'

urlpatterns = [
    path('crear/', crear_cliente, name='crear'),
    path('listar/', listar_cliente, name='listar')
]