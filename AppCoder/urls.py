from django.urls import path
from AppCoder import views

urlpatterns = [

    path('inicio',views.inicio, name="Inicio"),
    path('empleados', views.empleados, name="Empleados"),
    path('clientes', views.clientes, name="Clientes"),
    path('productos', views.productos, name="Productos"),

]