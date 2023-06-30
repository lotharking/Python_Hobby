from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:listar')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/crear_cliente.html', {'form':form})

def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes':clientes})