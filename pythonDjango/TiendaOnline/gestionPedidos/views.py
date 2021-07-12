from gestionPedidos.apps import GestionpedidosConfig
from TiendaOnline.settings import EMAIL_HOST_USER
from django.db.models import query
from gestionPedidos.models import Articulos
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    # implement method of search info of DB
    if request.GET["prd"]:
        # mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto) > 20:
            mensaje= "Texto de busqueda demasiado largo"
        else:
            articulos= Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        mensaje="No se ha introducido nada"
    return HttpResponse(mensaje)

def contacto(request):
    # implement tab of contact
    if request.method=="POST":
        # """implementacion de formulario con apiforms"""
        miFromulario=FormularioContacto(request.POST)

        if miFromulario.is_valid():

            infForm=miFromulario.cleaned_data

            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),["andresfelipe083195@hotmail.com"],)
            return render(request,"gracias.html")

            # """implementacion de metodo por peticion directa"""
            # asunto=request.POST['asunto']
            # mensaje=request.POST['mensaje'] + " " + request.POST['email']
            # email_from=EMAIL_HOST_USER
            # recipient_list=["andresfelipe083195@hotmail.com"]
            # send_mail(asunto,mensaje,email_from,recipient_list)

    else:
        miFromulario=FormularioContacto()
    
    return render(request, "formulario_contacto.html", {"form": miFromulario})


    # return render(request, "contacto.html")