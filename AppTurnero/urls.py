from django.urls import path, include
from AppTurnero.views import *

urlpatterns = [
path("", inicio, name ="Inicio"),
path('inicio/', inicio, name = "Inicio"),
path('profesionales/', profesional, name = "profesionales"),
path('horarios/', horario, name = "Horarios"),
path('agenda/', agenda, name = "Agenda"),
path('pacientes/', paciente, name = "Pacientes"),
path('contacto/', contactanos, name = "Contactanos"),
##path('profesionalFormulario/', formprofesional , name = "FormProfesional"),
]