from django.urls import path
from AppCoder import views

urlpatterns = [

    path('',views.inicio, name="Inicio"),
    path('empleadosFormulario', views.empleadosFormulario, name="EmpleadosFormulario"),
    path('clientesFormulario', views.clientesFormulario, name="ClientesFormulario"),
    path('productosFormulario', views.productosFormulario, name="ProductosFormulario"),
    path('buscar/', views.buscar),

]