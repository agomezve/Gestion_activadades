from django.contrib import admin
from .models import Actividad, Usuario, Monitor, Sala, ResponsableSala

admin.site.register(Actividad)
admin.site.register(Usuario)
admin.site.register(Monitor)
admin.site.register(Sala)
admin.site.register(ResponsableSala)