from django import views
from django.urls import path
from appClinica.views import inicio, tsolicitadoList,turnoForm,contacto,nosotros,admin,agregarPersonalForm,busquedaPacientes,detallePersonal,personalList,agregarPacienteForm,editarPersonal,eliminarPersonal,personalList2,detalleTsolicitud,eliminarTsolicitud,buscar,editarPaciente,eliminarPaciente, login_request,register_request,usuario,pacienteagregado,turnoconfirmado,turnoeliminado,pacienteeliminado,pacienteeditado,personaleliminado,personaleditado,personalagregado,editarPerfil,usuariomodificado
from django.contrib.auth.views import LogoutView
urlpatterns = [
    #------------------------------ URLS MAIN PAGE ------------------------------#
    path('', inicio, name='inicio'),
    path('turno/nuevo', turnoForm.as_view(), name='turno'),
    path('nosotros/', nosotros, name='nosotros'),
    path('profesionales/list', personalList.as_view(), name='profesionales'),
    path('contacto/', contacto, name='contacto'),

    #------------------------------ URLS ADMIN ------------------------------#
    path('adminpage/', admin, name='admin'), 
    path('usuario/', usuario, name='usuario'), 
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="appClinica/logout.html"), name='logout'),
    path('registrarse/', register_request, name='registrarse'),
    path('editarusuario/', editarPerfil, name='usuario_editar'),
    path('usuariomodificado/', usuariomodificado, name='usuariomodificado'),


    #------------------------------ URLS PACIENTES ADMIN ------------------------------#
    path('agregarpaciente/nuevo', agregarPacienteForm.as_view(), name='agregarpaciente'), 
    path('busquedaPacientes/', busquedaPacientes, name='pacientes'),
    path('buscar/', buscar, name='buscar'),
    path('busquedaPacientes/borrar/<pk>', eliminarPaciente.as_view(), name='paciente_eliminar'),
    path('pacienteeliminado/', pacienteeliminado, name='pacienteeliminado' ),
    path('busquedaPaciente/edicion/<pk>', editarPaciente.as_view(), name='paciente_editar'),
    path('pacienteeditado/', pacienteeditado, name='pacienteeditado' ),
    path('pacienteagregado/', pacienteagregado, name='pacienteagregado' ),


    #------------------------------ URLS TURNOS ADMIN ------------------------------#
    path('tsolicitado/list', tsolicitadoList.as_view(), name='tsolicitado'),
    path('tsolicitado_detalle/<pk>', detalleTsolicitud.as_view(), name='tsolicitado_detalle'),
    path('tsolicitado/borrar/<pk>', eliminarTsolicitud.as_view(), name='tsolicitado_eliminar'),
    path('turnoconfirmado/', turnoconfirmado, name='turnoconfirmado'),
    path('turnoeliminado/', turnoeliminado, name='turnoeliminado'),

    #------------------------------ URLS PERSONAL ADMIN ------------------------------#
    path('personal/list', personalList2.as_view(), name='personal'),
    path('personal_detalle/<pk>', detallePersonal.as_view(), name='personal_detalle'), 
    path('personal/nuevo', agregarPersonalForm.as_view(), name='personal_agregar'),
    path('personalagregado/', personalagregado, name='personalagregado'),
    path('personal/edicion/<pk>', editarPersonal.as_view(), name='personal_editar'),
    path('personaleditado/', personaleditado, name='personaleditado'),
    path('personal/borrar/<pk>', eliminarPersonal.as_view(), name='personal_eliminar'),
    path('personaleliminado/', personaleliminado, name='personaleliminado'),

]