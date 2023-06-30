from django import forms
from django.utils import timezone


class formsetProducto(forms.Form):
    nombre = forms.CharField(max_length=40)
    stock = forms.FloatField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField(max_length=80)
    createdAt = forms.DateTimeField(default=timezone.now)
