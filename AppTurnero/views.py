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

		valor1 = FormProfesionales(request.POST)
		
		if valor1.is_valid():
			info = valor1.cleaned_data
			DatosProfesionales=DatosProfesionales(nombre=info["fnombre"],apellido=info["fapellido"],mail=info["fmail"],cuit=info["fcuit"],razon_social=info["frazon_social"], especialidad=info["fespecialidad"])
			DatosProfesionales.save()
			return render(request,"AppTurnero/inicio.html")
	else:
		valor1 = FormProfesionales()

	return render (request,"AppTurnero/profesionalFormulario.html", {"registro1":valor1})

#	plantilla = loader.get_template("principal.html")
#	documento_1 = plantilla.render(Datos_profesionales)
#	return HttpResponse(documento_1)
