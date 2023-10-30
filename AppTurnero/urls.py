from django.urls import path, include
from AppTurnero.views import * ##inicio, InicioSesion, iniciop, contactanos, horario, agenda, paciente, profesional
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
path("", inicio, name ="Inicio"),
path('inicio/', inicio, name = "Inicio"),
path('login/', InicioSesion, name = "login"),
path('horarios/', horario, name = "Horarios"),
path('agenda/', agendad, name = "Agenda"),
path('pacientes/', paciente, name = "Pacientes"),
path('contacto/', contactanos, name = "Contactanos"),
path('horarios/', views.generar_horarios_disponibles, name='Generarhorarios'),

## CRUD DE PROFESIONALES ##
path('LeerProf/', leerProfesionales, name = "LeerProf"),
path('CrearProf/', CrearProfesionales, name = "CrearProf"),
path('profesionales/', profesional, name = "profesionales"),
path('eliminarProf/<nombreprof>', EliminarProfesionales, name = "EliminarProfesional"),
path('editarProf/<id_prof>', EditarProfesionales, name = "EditarProfesional"),


## CRUD DE PACIENTES ##
path('LeerPac/',leerPacientes, name="LeerPac"),
path('editarPac/<id_pac>', EditarPacientes, name = "EditarPacientes"),

##path('login/', inicioSesion, name = "Login"),
##path('register/', registro, name = "SignUp"),
path('logout/', LogoutView.as_view(), name = "Logout"),
##path('profesionalFormulario/', formprofesional , name = "FormProfesional"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

