from django.urls import path, include
from AppTurnero.views import *

urlpatterns = [
path("", inicio),
path('profesionales/', profesional),
path('horarios/', horario),
path('agenda/', agenda),
path('pacientes/', paciente),
]