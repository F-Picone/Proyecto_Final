from django.urls import path
from appClinica.views import inicio,turno,contacto,nosotros,profesionales,admin

urlpatterns = [
    path('', inicio, name='inicio'),
    path('turno/', turno, name='turno'),
    path('nosotros/', nosotros, name='nosotros'),
    path('profesionales/', profesionales, name='profesionales'),
    path('contacto/', contacto, name='contacto'),
    path('adminpage/', admin, name='admin'),
]