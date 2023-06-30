
from django.shortcuts import render, redirect
from TerceraPreEntregaManceboApp.models import Producto
from TerceraPreEntregaManceboApp.forms import formsetProducto
from django.contrib import messages
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
            messages.success(request, "Producto registrado exitosamente") 
            return redirect('Producto')
            
            
    
    miFormulario = formsetProducto()
    return render(request, 'AppTemplates/Producto.html',{'form': miFormulario})

def getProducto(request):
    return render(request, 'AppTemplates/getProducto.html')

        
    

def Venta(request):
    return render(request, "AppTemplates/Venta.html")

def DetalleVenta(request):
    return render(request, "AppTemplates/DetalleVenta.html")