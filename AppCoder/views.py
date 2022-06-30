import email
from django.shortcuts import render
from AppCoder.forms import EmpleadosFormulario, ClientesFormulario, ProductosFormulario
from AppCoder.models import Clientes, Empleados, Productos

# Create your views here.

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def empleadosFormulario(request):
    if request.method == 'POST':
        miFormulario = EmpleadosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado = Empleados (nombre=informacion['nombre'], apellido=informacion['apellido'], fechaIngreso=informacion['fechaIngreso'])
            empleado.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EmpleadosFormulario()
    return render(request, "AppCoder/empleadosFormulario.html", {"miFormulario":miFormulario})

def clientesFormulario(request):
    if request.method == 'POST':
        miFormulario = ClientesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Clientes (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            cliente.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ClientesFormulario()
    return render(request, "AppCoder/clientesFormulario.html", {"miFormulario":miFormulario})

def productosFormulario(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Productos (descripcion=informacion['descripcion'], codigo=informacion['codigo'], stock=informacion['stock'])
            producto.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProductosFormulario()
    return render(request, "AppCoder/productosFormulario.html", {"miFormulario":miFormulario})

def buscar(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        print(codigo)
        producto = Productos.objects.filter(codigo__icontains=codigo)
        print(producto)
        return render(request, "AppCoder/inicio.html", {"producto":producto, "codigo":codigo})
    else:
        respuesta = "NO SE ESPECIFICO CODIGO"
    return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})