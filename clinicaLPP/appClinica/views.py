from django.http import  HttpResponse
from django.template import loader,Context,Template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView,UpdateView
from appClinica.models import paciente, personal, solicitud_turno
from appClinica.forms import UserRegistrationForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#------------------ VIEWS MAIN PAGE ------------------#



def inicio(request):
    return render(request, 'appClinica/inicio.html')

def nosotros(request):
    return render(request, 'appClinica/nosotros.html')

def contacto(request):
    return render(request, 'appClinica/contacto.html')

class personalList(ListView):
    model = personal
    template_name = 'appClinica/personalList.html'



#------------------ VIEWS DE TURNO MAINPAGE ------------------#



def turnoconfirmado(request):
    return render(request, 'appClinica/turnoconfirmado.html')

class turnoForm(CreateView):
    model = solicitud_turno
    template_name = 'appClinica/turno_form.html'
    success_url = reverse_lazy('turnoconfirmado')
    fields = ['nombre', 'apellido', 'especialidad', 'email']



#------------------ VIEWS DE TURNO ADMIN ------------------#



class tsolicitadoList(LoginRequiredMixin, ListView):
    model = solicitud_turno
    template_name = "appClinica/tsolicitado.html"


class detalleTsolicitud(LoginRequiredMixin, DetailView):
    model = solicitud_turno
    template_name = "appClinica/tsolicitud_detalle.html"

class eliminarTsolicitud(LoginRequiredMixin, DeleteView):
    model = solicitud_turno
    template_name = 'appClinica/tsolicitado_confirm_delete.html'
    success_url = reverse_lazy('turnoeliminado')

def turnoeliminado(request):
    return render(request, 'appClinica/turnoeliminado.html')



#------------------ VIEWS ADMIN USUARIO ------------------#



def admin(request):
    return render(request, 'appClinica/admin.html')

def usuario(request):
    return render(request, 'appClinica/usuario.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave )
            if user is not None:
                login(request,user)
                return render(request, 'appClinica/admin.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'appClinica/admin.html', {'mensaje': 'Error, datos erroneos'})
        else:
            return render(request, 'appClinica/admin.html', {'mensaje': 'Error, datos erroneos'})
    else:
        form = AuthenticationForm()
        return render(request, "appClinica/login.html", {'form':form})

@login_required
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'appClinica/admin.html', {'mensaje': f'Usuario {username} creado'})
        else:
            return render(request, 'appClinica/admin.html', {'mensaje': 'Error, no se pudo crear el usuario'})
    else:
        form = UserRegistrationForm()
        return render(request, 'appClinica/register.html', {'form':form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'appClinica/usuariomodificado.html')
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'appClinica/editarusuario.html', {'formulario': formulario, 'usuario': usuario.username})

def usuariomodificado(request):
    return render(request, 'appClinica/usuariomodificado.html')









#------------------ VIEWS DE PACIENTES ADMIN ------------------#



class agregarPacienteForm(LoginRequiredMixin, CreateView):
    model = paciente
    template_name = 'appClinica/agregarpaciente_form.html'
    success_url = reverse_lazy('pacienteagregado')
    fields = ['nombre', 'apellido', 'dni', 'obra_social']

def pacienteagregado(request):
    return render(request, 'appClinica/pacienteagregado.html')

@login_required
def busquedaPacientes(request):
    return render(request, 'appClinica/busquedaPacientes.html')

@login_required
def buscar(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        pacientes= paciente.objects.filter(dni__icontains = dni)
        return render(request, "appClinica/resultadoBusqueda.html", {"dni":dni, "pacientes":pacientes})
    else:
        respuesta = 'No enviaste datos correctos'
    return  HttpResponse(respuesta)

class eliminarPaciente(LoginRequiredMixin, DeleteView):
    model = paciente
    template_name = 'appClinica/paciente_confirm_delete.html'
    success_url = reverse_lazy('pacienteeliminado')

def pacienteeliminado(request):
    return render(request, 'appClinica/pacienteeliminado.html')

class editarPaciente(LoginRequiredMixin, UpdateView):
    model = paciente
    template_name = 'appClinica/editarpaciente_form.html'
    success_url = reverse_lazy('pacienteeditado')
    fields = ['nombre', 'apellido', 'dni', 'obra_social']

def pacienteeditado(request):
    return render(request, 'appClinica/pacienteeditado.html')



#------------------ VIEWS DEL PERSONAL ADMIN ------------------#



class personalList2(LoginRequiredMixin, ListView):
    model = personal
    template_name = 'appClinica/personalList2.html'

class detallePersonal(LoginRequiredMixin, DetailView):
    model = personal
    template_name = "appClinica/personal_detalle.html"

class agregarPersonalForm(LoginRequiredMixin, CreateView):
    model = personal
    template_name = 'appClinica/agregarpersonal_form.html'
    success_url = reverse_lazy('personalagregado')
    fields = ['nombre', 'apellido', 'cargo', 'dni']

def personalagregado(request):
    return render(request, 'appClinica/personalagregado.html')

class editarPersonal(LoginRequiredMixin, UpdateView):
    model = personal
    template_name = 'appClinica/editarpersonal_form.html'
    success_url = reverse_lazy('personaleditado')
    fields = ['nombre', 'apellido', 'cargo', 'dni']

def personaleditado(request):
    return render(request, 'appClinica/personaleditado.html')

class eliminarPersonal(LoginRequiredMixin, DeleteView):
    model = personal
    template_name = 'appClinica/personal_confirm_delete.html'
    success_url = reverse_lazy('personaleliminado')

def personaleliminado(request):
    return render(request, 'appClinica/personaleliminado.html')



