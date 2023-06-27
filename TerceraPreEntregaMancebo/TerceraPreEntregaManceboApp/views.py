from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppTemplates/inicio.html")

def Cliente(request):
    return render(request, "AppTemplates/Cliente.html")

def Producto(request):
    return render(request, "AppTemplates/Producto.html")

def Venta(request):
    return render(request, "AppTemplates/Venta.html")

def DetalleVenta(request):
    return render(request, "AppTemplates/DetalleVenta.html")