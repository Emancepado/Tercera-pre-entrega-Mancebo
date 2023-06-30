
from django.shortcuts import render, redirect
from TerceraPreEntregaManceboApp.models import Producto
from TerceraPreEntregaManceboApp.forms import formsetProducto
# Create your views here.

def inicio(request):
    return render(request, "AppTemplates/inicio.html")

def producto(request):
    if request.method == 'POST':
        miFormulario = formsetProducto(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            product = Producto(nombre=data["nombre"], stock= data["stock"], price= data["price"], description = request.POST["description"])
            product.save()
            return redirect(request,'/Producto')
    else:
        miFormulario = formsetProducto()
        
    

def Venta(request):
    return render(request, "AppTemplates/Venta.html")

def DetalleVenta(request):
    return render(request, "AppTemplates/DetalleVenta.html")