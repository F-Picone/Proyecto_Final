from django.contrib import admin
from .models import medico,paciente,solicitud_turno
# SUPER USER:   User: Franco
#               email: piconito.f@gmail.com
#               password: 123456
admin.site.register(medico)

admin.site.register(paciente)

admin.site.register(solicitud_turno)