from django import forms


class DatosProfesionalesForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    mail = forms.EmailField()
    cuit = forms.CharField(max_length=11)
    razon_social = forms.CharField(max_length=60)
    especialidad = forms.CharField(max_length=60)

class DatosPacientesForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    obra_social = forms.CharField(max_length=60)
    numero_os = forms.IntegerField(default=0)
    avatar = forms.ImageField(default="{% static 'AppTurnero/ava1.jpeg' %}")