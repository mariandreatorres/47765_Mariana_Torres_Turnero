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
        #model = Pacientes
        nombre = forms.CharField(max_length=60)
        apellido = forms.CharField(max_length=60)
        obra_social = forms.CharField(max_length=60)
        numero_os = forms.IntegerField()
        avatar = forms.ImageField(required=False)
        #fields = ['nombre', 'apellido', 'obra_social', 'numero_os', 'avatar']
    # Añade una validación opcional para el archivo, si es necesario
        def clean_avatar(self):
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                if avatar and avatar.size > 102400:
                    raise forms.ValidationError("El archivo es demasiado grande. El tamaño máximo permitido es de {} bytes.".format(102400))
            if avatar:
                allowed_types = ['image/jpeg', 'image/png', 'image/gif']
            if avatar.content_type not in allowed_types:
                raise forms.ValidationError("El archivo debe ser una imagen en formato JPEG, PNG o GIF.")

            else:    # Realiza las validaciones necesarias aquí (tamaño, tipo, etc.)
                pass
            return avatar
    


    
    
