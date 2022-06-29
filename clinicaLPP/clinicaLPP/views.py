from django.http import  HttpResponse
from django.template import loader,Context,Template


def probandoTemplate(self):
    diccionario = {'nombre':'nombre'}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)