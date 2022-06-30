from django.urls import path
from appClinica.views import inicio,turno,contacto,nosotros,profesionales,admin,tsolicitado,agregarpaciente,pacientes,personal

urlpatterns = [
    path('', inicio, name='inicio'),
    path('turno/', turno, name='turno'),
    path('nosotros/', nosotros, name='nosotros'),
    path('profesionales/', profesionales, name='profesionales'),
    path('contacto/', contacto, name='contacto'),
    #------------------------------ URLS ADMIN ------------------------------#
    path('adminpage/', admin, name='admin'),
    path('tsolicitado/', tsolicitado, name='tsolicitado'), #VER TURNOS SOLICITAOOS
    path('agregarpaciente/', agregarpaciente, name='agregarpaciente'), #AGREGAR PACIENTE
    path('pacientes/', pacientes, name='pacientes'), #BUSCAR PACIENTES /ELIMINAR/EDITAR/
    path('personal/', personal, name='personal'), #PERSONAL /AGREGAR/SACAR/EDITAR
]