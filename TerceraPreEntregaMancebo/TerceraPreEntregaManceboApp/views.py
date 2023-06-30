from django.shortcuts import render
from django.shortcuts import render
from TerceraPreEntregaManceboApp.models import Producto

# Create your views here.

def inicio(request):
    return render(request, "AppTemplates/inicio.html")

def Producto(request):
    if request.method == 'POST':
        Product = Producto(nombre=request.POST["nombre"], stock= request.POST["stock"], price= request.POST["price"], description = request.POST["description"])
        Product.save()
        return render(request, "AppTemplates/Producto.html")
    return render(request, "AppTemplates/Producto.html")

def Venta(request):
    return render(request, "AppTemplates/Venta.html")

def DetalleVenta(request):
    return render(request, "AppTemplates/DetalleVenta.html")