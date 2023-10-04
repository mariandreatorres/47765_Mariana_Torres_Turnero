from django import forms


class DatosProfesionalesForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField()
    cuit = forms.CharField(max_length=11)
    razon_social = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)

