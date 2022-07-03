from django import views
from django.urls import path
from appClinica.views import inicio, tsolicitadoList,turnoForm,contacto,nosotros,admin,agregarPersonalForm,busquedaPacientes,detallePersonal,personalList,agregarPacienteForm,editarPersonal,eliminarPersonal,personalList2,detalleTsolicitud,eliminarTsolicitud,buscar

urlpatterns = [
    #------------------------------ URLS MAIN PAGE ------------------------------#
    path('', inicio, name='inicio'),
    path('turno/nuevo', turnoForm.as_view(), name='turno'),
    path('nosotros/', nosotros, name='nosotros'),
    path('profesionales/list', personalList.as_view(), name='profesionales'),
    path('contacto/', contacto, name='contacto'),

    #------------------------------ URLS ADMIN ------------------------------#
    path('adminpage/', admin, name='admin'), #VER TURNOS SOLICITAOOS

    #------------------------------ URLS PACIENTES ADMIN ------------------------------#
    path('agregarpaciente/nuevo', agregarPacienteForm.as_view(), name='agregarpaciente'), 
    path('busquedaPacientes/', busquedaPacientes, name='pacientes'),
    path('buscar/', buscar, name='buscar'),
    path('tsolicitado/list', tsolicitadoList.as_view(), name='tsolicitado'),
    path('tsolicitado_detalle/<pk>', detalleTsolicitud.as_view(), name='tsolicitado_detalle'),
    path('tsolicitado/borrar/<pk>', eliminarTsolicitud.as_view(), name='tsolicitado_eliminar'),

    #------------------------------ URLS PERSONAL ADMIN ------------------------------#
    path('personal/list', personalList2.as_view(), name='personal'),
    path('personal_detalle/<pk>', detallePersonal.as_view(), name='personal_detalle'), 
    path('personal/nuevo', agregarPersonalForm.as_view(), name='personal_agregar'),
    path('personal/edicion/<pk>', editarPersonal.as_view(), name='personal_editar'),
    path('personal/borrar/<pk>', eliminarPersonal.as_view(), name='personal_eliminar'),
]