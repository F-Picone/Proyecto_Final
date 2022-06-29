from django.contrib import admin
from django.urls import path
from clinicaLPP.views import probandoTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', probandoTemplate),
]
