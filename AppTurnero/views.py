from django.shortcuts import render
from django.http import HttpResponse
from AppTurnero.models import DatosProfesionales, HorariosProfesionales, Meses, Pacientes
from django.template import Template, Context, loader
#from django.contrib import admin
from datetime import datetime

def inicio(request):
	return render (request,"Appturnero/inicio.html")

def profesional(request):  ###prueba
	valor_1 = DatosProfesionales (nombre="Mariana", 
		 apellido ="Torres",
    	 mail = "mariandreatorres@gmail.com",
		 cuit = '27223707489',
		 razon_social ='Torres, Mariana Andrea',
		 especialidad = 'Ortodoncista')
	valor_1.save()
	return render (request,"Appturnero/profesionales.html")

	
	plantilla = loader.get_template("principal.html")
	documento_1 = plantilla.render(Datos_profesionales)
	return HttpResponse(documento_1)

def horario(request):
	return render (request,"AppTurnero/horarios.html")

def agenda(request):
	return render (request,"AppTurnero/agenda.html")

def paciente(request):
	return render (request,"AppTurnero/pacientes.html")
    
def turnos(request):
	return render (request,"AppTurnero/turnos.html")

