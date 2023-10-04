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

def profesional(request):
    if request.method == 'POST':
        form = DatosProfesionalesForm(request.POST)
        if form.is_valid():
            # Guardamos los datos
            DatosProfesionalesForm.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                mail=form.cleaned_data['mail'],
                cuit=form.cleaned_data['cuit'],
                razon_social=form.cleaned_data['razon_social'],
                especialidad=form.cleaned_data['especialidad']
            )
            # Redireccionamos a la misma página después de guardar
            return redirect('profesionales')

    else:
        form = DatosProfesionalesForm()

    return render(request, "AppTurnero/profesionales.html", {'form': form})


