from django import forms

class FormProfesionales(forms.Form):

    fnombre = forms.CharField()
    fapellido = forms.CharField()
    fmail = forms.CharField()
    fcuit = forms.CharField()
    frazon_social = forms.CharField()
    fespecialidad = forms.CharField()
