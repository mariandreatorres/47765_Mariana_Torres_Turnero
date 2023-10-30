from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from AppTurnero.models import DatosProfesionales, HorariosProfesionales, AgendaAsignada, AgendaDisponible, Pacientes
from AppTurnero.forms import *
from django.template import Template, Context, loader
#from django.contrib import admin
from datetime import datetime, timedelta
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate





def inicio(request):
	return render (request,"Appturnero/inicio.html")

def iniciop(request):
	return render (request,"Appturnero/iniciop.html")

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
                numero_os=infopac['numero_os'],
                avatar=infopac['avatar'])
            # Redireccionamos a la misma página después de guardar
            return render(request, "AppTurnero/inicio.html")

    else:
        print(form.errors)
        form = DatosPacientesForm()

    return render(request, "AppTurnero/pacientes.html", {'form': form})

def leerPacientes(request):
     pacientes = Pacientes.objects.all() ##clase 22##
     listado = {"pacientes":pacientes}
     return render(request, "AppTurnero/leerpacientes.html",listado)

#class ListaPacienes(ListView):
#     model = Pacientes

#class DetallePacientes(DetailView):
#     model = Pacientes

#class CrearPaciente(CreateView):
#     model = Pacientes
#     success_url = "AppTurnero/pacient/list"
#     fields = ["id", "nombre", "apellido","obra_social", "numero_os","avatar"]
    


def leerProfesionales(request):
     profesionales = DatosProfesionales.objects.all()
     contexto = {"professional":profesionales}
     return render(request, "AppTurnero/leerProfesionales.html",contexto)
##def ActualizarPacientes(request):
     
##def EliminarPacientes(request):



#def editarusuario(request):
#     usuario = request.user
#     if request.method == 'POST':
#          form = FormEditarUsuario()

#def BuscarHorarios(request):
#     if request.GET["horario"]:
#          agenda = AgendaForm

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

def CrearProfesionales(request):
     if request.method == 'POST':
        formprof = DatosProfesionalesForm(request.POST)
        if formprof.is_valid():
             info = formprof.cleaned_data
             profesional = DatosProfesionales(nombre=info['nombre'],
                apellido=info['apellido'],
                mail=info['mail'],
                cuit=info['cuit'],
                razon_social=info['razon_social'],
                especialidad=info['especialidad'] )
             profesional.save()
             return render(request,"AppTurnero/inicio.html")
     else:
          formprof = DatosProfesionalesForm()

     return render(request, "AppTurnero/crearprofesionales.html", {'formprof': formprof})   

def EliminarProfesionales(request, nombreprof):
     profesional = DatosProfesionales.objects.get(nombre=nombreprof)
     profesional.delete()

     profesionales = DatosProfesionales.objects.all()

     listado = {"nombre":profesionales}
     return render(request, "AppTurnero/leerProfesionales.html",{'profesionales': profesionales})

def EditarProfesionales(request, nombreprof):
     profesional = DatosProfesionales.objects.get(nombre=nombreprof)
     if request.method == 'POST':
        miformulario =  DatosProfesionalesForm(request.POST, instance=profesional)
        if miformulario.is_valid():
             info = miformulario.cleaned_data
             profesional.nombre =info['nombre'],
             profesional.apellido=info['apellido'],
             profesional.mail=info['mail'],
             profesional.cuit=info['cuit'],
             profesional.razon_social=info['razon_social'],
             profesional.especialidad=info['especialidad'] 
             profesional.save()
             return render(request,"AppTurnero/inicio.html")
     else:
          miformulario = DatosProfesionalesForm(instance=profesional)
               
               #initial={"nombre":profesional.nombre,
               #                                          "apelliido":profesional.apellildo,
               #                                          "mail":profesional.mail,
               #                                          "cuit":profesional.cuit,
               #                                          "razon_social":profesional.razon_social,
               #                                          "especialidad":profesional.especialidad,})

  
     return render(request, "AppTurnero/EditarProfesionales.html",{'miformulario': miformulario, 'profesional': profesional})



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

def busquedaMisTurnos(request):
     return render( request, "AppTurnero/busquedaMisTurnos.html")

##def resultadoMisTurnos(request):


##def CrearAgendaDisponible(request):


def generar_horarios_disponibles(request, id_profesional, fecha):
    # Obtener el profesional
    profesional = HorariosProfesionales.objects.get(id=id_profesional)

    # Obtener la agenda del profesional para la fecha especificada
    agenda = AgendaDisponible.objects.filter(profesional=id_profesional, dia=fecha)

    # Calcular los horarios disponibles
    horarios_disponibles = []
    hora_actual = profesional.hora_inicio
    hora_fin = profesional.hora_fin

    while hora_actual < hora_fin:
        disponible = True
        for cita in agenda:
            if hora_actual >= cita.hora_inicio and hora_actual < cita.hora_fin:
                disponible = False
                break

        if disponible:
            horario_disponible = AgendaDisponible(
                profesional=profesional,
                fecha=fecha,
                hora=hora_actual,
                disponibilidad='Y'
            )
            horario_disponible.save()
            horarios_disponibles.append(horario_disponible)

        hora_actual += timedelta(minutes=HorariosProfesionales.duracion_consulta)  # Puedes ajustar el intervalo de tiempo según tus necesidades

    return render(request, 'AppTurnero/horarios_disponibles.html', {'id_profesional': profesional, 'fecha': fecha, 'horarios_disponibles': horarios_disponibles})