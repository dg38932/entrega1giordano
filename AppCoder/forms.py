from django import forms

class EmpleadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    fechaIngreso = forms.DateField()

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class ProductosFormulario(forms.Form):
    descripcion = forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    stock = forms.IntegerField()