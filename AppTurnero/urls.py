from django.urls import path, include
from AppTurnero.views import *

urlpatterns = [
path("", inicio, name ="Inicio"),
path('inicio/', inicio, name = "Inicio"),
path('profesionales/', profesional, name = "Profesionales"),
path('horarios/', horario, name = "Horarios"),
path('agenda/', agenda, name = "Agenda"),
path('pacientes/', paciente, name = "Pacientes"),
]