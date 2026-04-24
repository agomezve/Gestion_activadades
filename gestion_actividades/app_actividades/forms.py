from django import forms
from .models import Actividad, Usuario, Monitor, Sala, ResponsableSala

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ResponsableSalaForm(forms.ModelForm):
    class Meta:
        model = ResponsableSala
        fields = '__all__'

class InscripcionForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True, label="Seleccionar Usuario a Inscribir")
