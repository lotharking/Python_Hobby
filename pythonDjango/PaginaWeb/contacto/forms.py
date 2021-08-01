from django import forms
from django.forms.fields import EmailField

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Correo", required=True)
    contenido=forms.CharField(label="Contenido")