from django.http import  HttpResponse
from django.template import loader,Context,Template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView,UpdateView
from appClinica.models import paciente, personal, solicitud_turno
from appClinica.forms import PacienteFormulario


#VIEWS MAIN PAGE

def inicio(request):
    return render(request, 'appClinica/inicio.html')

def nosotros(request):
    return render(request, 'appClinica/nosotros.html')

def contacto(request):
    return render(request, 'appClinica/contacto.html')

class personalList(ListView):
    model = personal
    template_name = 'appClinica/personalList.html'


#VIEWS DE TURNO MAINPAGE

class turnoForm(CreateView):
    model = solicitud_turno
    template_name = 'appClinica/turno_form.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellido', 'especialidad', 'email']

#VIEWS DE TURNO ADMIN

class tsolicitadoList(ListView):
    model = solicitud_turno
    template_name = "appClinica/tsolicitado.html"


class detalleTsolicitud(DetailView):
    model = solicitud_turno
    template_name = "appClinica/tsolicitud_detalle.html"

class eliminarTsolicitud(DeleteView):
    model = solicitud_turno
    template_name = 'appClinica/tsolicitado_confirm_delete.html'
    success_url = reverse_lazy('tsolicitado')


#VIEWS ADMIN Y LOGIN/LOGUOT

def admin(request):
    return render(request, 'appClinica/admin.html')


#VIEWS DE PACIENTES MAIN PAGE

class agregarPacienteForm(CreateView):
    model = paciente
    template_name = 'appClinica/agregarpaciente_form.html'
    success_url = reverse_lazy('pacientes')
    fields = ['nombre', 'apellido', 'dni', 'obra_social']

#VIEWS DE PACIENTES ADMIN

def busquedaPacientes(request):
    return render(request, 'appClinica/busquedaPacientes.html')

def buscar(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        pacientes= paciente.objects.filter(dni__icontains = dni)
        return render(request, "appClinica/resultadoBusqueda.html", {"dni":dni, "pacientes":pacientes})
    else:
        respuesta = 'No enviaste datos correctos'
    return  HttpResponse(respuesta)


#VIEWS DEL PERSONAL ADMIN
class personalList2(ListView):
    model = personal
    template_name = 'appClinica/personalList2.html'

class detallePersonal(DetailView):
    model = personal
    template_name = "appClinica/personal_detalle.html"

class agregarPersonalForm(CreateView):
    model = personal
    template_name = 'appClinica/agregarpersonal_form.html'
    success_url = reverse_lazy('personal')
    fields = ['nombre', 'apellido', 'cargo', 'dni']

class editarPersonal(UpdateView):
    model = personal
    template_name = 'appClinica/editarpersonal_form.html'
    success_url = reverse_lazy('personal')
    fields = ['nombre', 'apellido', 'cargo', 'dni']

class eliminarPersonal(DeleteView):
    model = personal
    template_name = 'appClinica/personal_confirm_delete.html'
    success_url = reverse_lazy('personal')



