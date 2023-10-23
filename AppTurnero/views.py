from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from AppTurnero.models import DatosProfesionales, HorariosProfesionales, AgendaAsignada, AgendaDisponible, Pacientes
from AppTurnero.forms import *
from django.template import Template, Context, loader
#from django.contrib import admin
from datetime import datetime, timedelta
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import EditView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def inicio(request):
	return render (request,"Appturnero/inicio.html")

def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
             user = form.cleaned_data.get("username")
             pwd =  form.cleaned_data.get("password")
             usuario = authenticate(request, username = user,password = pwd)
        
             if usuario is not None:
                 login(request,usuario)
                 return render(request,"AppTurnero/inicio.hmtl",{"Mensaje":f"Bienvenido (usuario)"})
        else:
             return render(request,"AppTurnero/inicio.html",{"Mensaje":"Usuario Incorrecto."})
    else:
       form = AuthenticationForm()  
    return render(request,"AppTurnero/login.html",{"formulario":form})

def horario(request):
	return render (request,"AppTurnero/horarios.html")

def contactanos(request):
	return render (request,"AppTurnero/contactanos.html")

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
                numero_os=infopac['numero_afiliado_os'],
                avatar=infopac['avatar'])
            # Redireccionamos a la misma página después de guardar
            return render(request, "AppTurnero/inicio.html")

    else:
        print(form.errors)
        form = DatosPacientesForm()

    return render(request, "AppTurnero/pacientes.html", {'form': form})

def leerProfesionales(request):
     profesionales = DatosProfesionales.objects.all()
     contexto = {"professional":profesionales}
     return render(request, "AppTurnero/leerProfesionales.html",contexto)

#def BuscarHorarios(request):
#     if request.GET["horario"]:
#          agenda = AgendaForm


def iniciop(request):
	return render (request,"Appturnero/iniciop.html")

def profesional(request):
    form=DatosProfesionalesForm()
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
        print(form.errors)
        form = DatosProfesionalesForm()

    return render(request, "AppTurnero/profesionales.html", {'form': form})

#def editarusuario(request):
#     usuario = request.user
#     if request.method == 'POST':
#          form = FormEditarUsuario()
 
def agendad(request):
    
    form1 = AgendaDisponibleForm()
    if request.method == "POST":
        form1 = AgendaDisponibleForm(request.POST,request.FILES)
    
        if form1.is_valid():
            # Guardamos los datos
            infoag = form1.cleaned_data
            # Crear una instancia del modelo y luego guardarla
            agenda = AgendaDisponible(
                id_agenda=infoag['IdAgenda'],
                id_profesional=infoag['Profesional'],
                fecha=infoag['Fecha'],
                hora=infoag['Hora'],
                disponibilidad=infoag['Disponible'] )
            agenda.save()
            
            return render(request, "AppTurnero/inicio.html")
        else:
            print(form1.errors)
            form1 = AgendaDisponibleForm()
    return render(request, "AppTurnero/agenda.html", {'form': form1})


