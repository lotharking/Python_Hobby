from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def Contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de la app", 
            "El usuario con el nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "", ["andresfelipe083195@gmail.com"],reply_to=[email]) # Direccion a donde va a llegar

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")                

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})