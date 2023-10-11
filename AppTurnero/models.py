from django.db import models
from datetime import datetime

class DatosProfesionales(models.Model):
    def __str__(self):

        return f"Nombre: {self.nombre} -- Apellido:{self.apellido} -- Mail: {self.mail} -- Cuit: {self.cuit} -- Razon Social: {self.razon_social}  --  Especialidad: {self.especialidad}"
    id_profesional = models.AutoField(primary_key=True)
    nombre = models.CharField(default="", max_length=60)
    apellido = models.CharField(default="", max_length=60)
    mail = models.EmailField(default="", max_length=100)
    cuit = models.CharField(default="", max_length=11)
    razon_social = models.CharField(default="", max_length=60)
    especialidad = models.CharField(default="", max_length=60)

class HorariosProfesionales(models.Model):
    def __str__(self):

        return f"id_profesional: {self.id_profesional} -- Dia de la semana: {self.dia_semana} -- hora_inicio: {self.hora_inicio} -- hora_fin: {self.hora_fin} "
    id_profesional = models.ForeignKey(DatosProfesionales, on_delete=models.CASCADE)
    dia_semana = models.CharField(default="", max_length=10)
    hora_inicio = models.TimeField(default=datetime.now)
    hora_fin = models.TimeField(default=datetime.now)

class Meses(models.Model):
    def __str__(self):

        return f"periodo: {self.periodo} -- id_profesional: {self.id_profesional} -- fecha: {self.fecha}  -- hora: {self.hora}"

    periodo = models.CharField(default="202301", max_length=10)
    id_profesional = models.ForeignKey(DatosProfesionales, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.today)
    hora = models.TimeField(default=datetime.now)

class Pacientes(models.Model):
    def __str__(self):

        return f"id_paciente: {self.id_paciente} -- nombre: {self.nombre} -- apellido: {self.apellido} -- obra social: {self.obra_social} -- numero obra social: {self.numero_os} -- avatar: {self.avatar}"
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(default="", max_length=60)
    apellido = models.CharField(default="", max_length=60)
    obra_social = models.CharField(default="", max_length=60)
    numero_os = models.IntegerField(default=0)
    avatar = models.ImageField(default="{% static 'AppTurnero/ava1.jpeg' %}")


