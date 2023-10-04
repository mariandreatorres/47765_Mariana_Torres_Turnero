from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from AppTurnero.models import DatosProfesionales, HorariosProfesionales, Meses, Pacientes
from AppTurnero.forms import *
from django.template import Template, Context, loader
#from django.contrib import admin
from datetime import datetime

def inicio(request):
	return render (request,"Appturnero/inicio.html")

#def profesional(request):  ###prueba
#	return render (request,"Appturnero/profesionales.html")


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

def profesional(request):
    if request.method == 'POST':
        form = DatosProfesionalesForm(request.POST)
    
        if form.is_valid():
            # Guardamos los datos
            info = form.cleaned_data
            DatosProfesionales.objects.create(
				nombre=info['nombre'],
                apellido=info['apellido'],
                mail=info['mail'],
                cuit=info['cuit'],
                razon_social=info['razon_social'],
                especialidad=info['especialidad']          )
			# Redireccionamos a la misma página después de guardar
            
            return render(request,"AppTurnero/inicio.html")

    else:
        form = DatosProfesionalesForm()

    return render(request, "AppTurnero/profesionales.html", {'form': form})


 