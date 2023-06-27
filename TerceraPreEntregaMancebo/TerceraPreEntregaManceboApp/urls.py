from django.urls import path
from TerceraPreEntregaManceboApp.views import inicio, Cliente, Venta, DetalleVenta, Producto

urlpatterns = [
    path('inicio/', inicio),
    path('Cliente/', Cliente),
    path('Venta/', Venta ),
    path('DetalleVenta/', DetalleVenta),
    path('Producto/', Producto),
    
]

