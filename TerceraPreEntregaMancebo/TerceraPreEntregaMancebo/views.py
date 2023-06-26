from django.http import HttpResponse
import datetime
from django.template import Template, Context


def showDia(request):
    dia = datetime.datetime.now()
    return HttpResponse(f"<h1>Hoy es {dia} <h1>")

def templatest(slef):
    mihtml = open("C:/Users/franc/OneDrive/Escritorio/VscodeShiet/TerceraPreEntregaMancebo/TerceraPreEntregaMancebo/plantillas/template1.html")

    plantilla = Template(mihtml.read())
    mihtml.close()
    micontext = Context()
    documento = plantilla.render(micontext)
    return HttpResponse(documento)

