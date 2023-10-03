from django.shortcuts import render
from django.http import HttpResponse
from AppTurnero.models import DatosProfesionales, HorariosProfesionales, Meses, Pacientes
from AppTurnero.forms import *
from django.template import Template, Context, loader
#from django.contrib import admin
from datetime import datetime

def inicio(request):
	return render (request,"Appturnero/inicio.html")

def profesional(request):  ###prueba
	return render (request,"Appturnero/profesionales.html")

	
	plantilla = loader.get_template("principal.html")
	documento_1 = plantilla.render(Datos_profesionales)
	return HttpResponse(documento_1)

def horario(request):
	return render (request,"AppTurnero/horarios.html")

def contactanos(request):
	return render (request,"AppTurnero/contactanos.html")

def agenda(request):
	return render (request,"AppTurnero/agenda.html")

def paciente(request):
	return render (request,"AppTurnero/pacientes.html")
    

def iniciop(request):
	return render (request,"Appturnero/iniciop.html")

def formprofesional(request):
	
	if request.method == "POST":

		valor_1 = FormProfesionales(request.POST)
		
		if valor_1.is_valid():
			info = valor_1.cleaned_data
			DatosProfesionales=DatosProfesionales[[]]
			DatosProfesionales.save()
			return render(request,"AppTurnero/inicio.html")
	
	return render (request,"AppTurnero/profesionalFormulario.html")