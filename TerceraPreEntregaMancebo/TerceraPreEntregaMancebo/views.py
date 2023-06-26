from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


def showDia(request):
    dia = datetime.datetime.now()
    return HttpResponse(f"<h1>Hoy es {dia} <h1>")

def templatest(slef):
    
    
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render()
    return HttpResponse(documento)

