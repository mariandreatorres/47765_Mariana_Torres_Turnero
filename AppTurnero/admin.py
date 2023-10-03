from django.contrib import admin
# Register your models here.

from AppTurnero.models import *

admin.site.register(DatosProfesionales)
admin.site.register(HorariosProfesionales)
admin.site.register(Meses)
admin.site.register(Pacientes)

