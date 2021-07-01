from django.http import HttpResponse
import datetime
from django.template import Template, context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): 
    p1 = Persona ("Andres", "Vallecilla")
    # nombre = "Juan"
    # apellido = "Velez"
    fecha_actual = datetime.datetime.now() 
    doc_externo = open("C:/Users/ANDRE/OneDrive/Documentos/GIT/Python_Hobby/pythonDjango/Proyecto1/Proyecto1/plantillas/primeraPlantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = context.Context({"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha": fecha_actual})
    documento = plt.render(ctx)
    return HttpResponse(documento)

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