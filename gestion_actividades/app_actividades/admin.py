from django.contrib import admin
from .models import UsuarioInscrito, Monitor, ResponsableSala, Sala, Actividad

admin.site.register(UsuarioInscrito)
admin.site.register(Monitor)
admin.site.register(ResponsableSala)
admin.site.register(Sala)
admin.site.register(Actividad)