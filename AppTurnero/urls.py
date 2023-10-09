from django.urls import path, include
from AppTurnero.views import inicio, InicioSesion, iniciop, contactanos, horario, agenda, paciente, profesional
from django.conf import settings
from django.conf.urls.static import static


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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

