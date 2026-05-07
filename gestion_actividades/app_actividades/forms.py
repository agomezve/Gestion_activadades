from django import forms
from .models import Actividad, Usuario, Monitor, Sala

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'edad', 'email', 'telefono']  

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class InscripcionForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True, label="Seleccionar Usuario a Inscribir")
