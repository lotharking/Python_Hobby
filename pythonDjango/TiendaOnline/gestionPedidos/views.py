from django.db.models import query
from gestionPedidos.models import Articulos
from django.http import HttpResponse
from django.shortcuts import render

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
        return render(request,"gracias.html")
    return render(request, "contacto.html")