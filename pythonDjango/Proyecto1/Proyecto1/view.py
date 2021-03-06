from django import template
from django.http import HttpResponse
import datetime
from django.template import Template, context, loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): 
    p1 = Persona ("Andres", "Vallecilla")
    # nombre = "Juan"
    # apellido = "Velez"
    fecha_actual = datetime.datetime.now() 
    temas_curso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    # doc_externo = open("C:/Users/ANDRE/OneDrive/Documentos/GIT/Python_Hobby/pythonDjango/Proyecto1/Proyecto1/template/primeraPlantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # doc_externo = loader.get_template('primeraPlantilla.html')
    # ctx = context.Context({"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha": fecha_actual, "temas": temas_curso})
    # documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha": fecha_actual, "temas": temas_curso})
    return render(request, "primeraPlantilla.html",{"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha": fecha_actual, "temas": temas_curso})

def cursoC(request):
    fecha_actual = datetime.datetime.now() 
    return render(request, "cursoC.html", {"fecha": fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now() 
    return render(request, "cursoCss.html", {"fecha": fecha_actual})

def despedida(request):
    return HttpResponse("Hasta luego")

def tiempo(request):
    fecha_actual = datetime.datetime.now() 
    documento = """<html>
    <body>
    <h1>    
    fecha actual %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, agno, edad):
    periodo = agno -2021
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h1>    
    En el año {} tendras {} años
    </h1>
    </body>
    </html>""".format(agno, edadFutura)
    return HttpResponse(documento)