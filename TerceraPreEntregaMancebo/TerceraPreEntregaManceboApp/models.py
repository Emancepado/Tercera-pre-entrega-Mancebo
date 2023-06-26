from django.db import models
from django.utils import timezone

#Create your models here
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, default='')
    email = models.EmailField()

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    stock = models.FloatField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='DetalleVenta')

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=8, decimal_places=2)
