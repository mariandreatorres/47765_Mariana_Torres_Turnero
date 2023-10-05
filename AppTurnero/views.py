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


def horario(request):
	return render (request,"AppTurnero/horarios.html")

def contactanos(request):
	return render (request,"AppTurnero/contactanos.html")

def agenda(request):
	return render (request,"AppTurnero/agenda.html")


def paciente(request):
    form= DatosPacientesForm()
    if request.method == 'POST':
        form = DatosPacientesForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Guardamos los datos
            infopac = form.cleaned_data
            Pacientes.objects.create(
                nombre=infopac['nombre'],
                apellido=infopac['apellido'],
                obra_social=infopac['obra_social'],
                numero_os=infopac['numero_os'],
                avatar=infopac['avatar'])
            # Redireccionamos a la misma página después de guardar
            return render(request, "AppTurnero/inicio.html")

    else:
        print(form.errors)
        form = DatosPacientesForm()

    return render(request, "AppTurnero/pacientes.html", {'form': form})



def iniciop(request):
	return render (request,"Appturnero/iniciop.html")

def profesional(request):
    form=DatosPacientesForm()
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


 