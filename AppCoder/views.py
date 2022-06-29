from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def empleados(request):
    return render(request, "AppCoder/empleados.html")

def clientes(request):
    return render(request, "AppCoder/clientes.html")
    
def productos(request):
    return render(request, "AppCoder/productos.html")

