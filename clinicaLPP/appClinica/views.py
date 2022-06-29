from django.http import  HttpResponse
from django.template import loader,Context,Template
from django.shortcuts import render




def inicio(request):
    return render(request, 'appClinica/inicio.html')
