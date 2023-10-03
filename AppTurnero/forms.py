from django import forms

class FormProfesionales(forms.form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.CharField()
    cuit = forms.CharField()
    razon_social = forms.CharField()
    especialidad = forms.CharField()
