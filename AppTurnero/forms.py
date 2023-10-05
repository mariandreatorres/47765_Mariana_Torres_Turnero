from django import forms
from .models import *


class DatosProfesionalesForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    mail = forms.EmailField()
    cuit = forms.CharField(max_length=11)
    razon_social = forms.CharField(max_length=60)
    especialidad = forms.CharField(max_length=60)

class DatosPacientesForm(forms.Form):
    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellido', 'obra_social', 'numero_os', 'avatar']
    # Añade una validación opcional para el archivo, si es necesario
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            # Realiza las validaciones necesarias aquí (tamaño, tipo, etc.)
            pass
        return avatar
    #nombre = forms.CharField(max_length=60)
    #apellido = forms.CharField(max_length=60)
    #obra_social = forms.CharField(max_length=60)
    #numero_os = forms.IntegerField(default=0)
    #avatar = forms.ImageField(default="{% static 'AppTurnero/ava1.jpeg' %}")


    
    
