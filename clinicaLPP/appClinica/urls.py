from django.urls import path
from appClinica.views import inicio

urlpatterns = [
    path('', inicio),
]