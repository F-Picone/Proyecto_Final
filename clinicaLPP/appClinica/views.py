from django.http import  HttpResponse
from django.template import loader,Context,Template
from django.shortcuts import render




def inicio(request):
    return render(request, 'appClinica/inicio.html')

def nosotros(request):
    return render(request, 'appClinica/nosotros.html')

def profesionales(request):
    return render(request, 'appClinica/profesionales.html')

def turno(request):
    return render(request, 'appClinica/turno.html')

def contacto(request):
    return render(request, 'appClinica/contacto.html')

def admin(request):
    return render(request, 'appClinica/admin.html')
