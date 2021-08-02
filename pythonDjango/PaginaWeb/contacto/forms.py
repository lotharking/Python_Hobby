from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Correo", required=True)
    contenido=forms.CharField(label="Contenido", widget=Textarea)