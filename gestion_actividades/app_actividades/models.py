from django.db import models

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100, default='')
    telefono = models.CharField(max_length=15, blank=True, default='')

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)

    def numero_actividades_asignadas(self):
        return self.actividades.count()

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    plazas_disponibles = models.IntegerField()
    
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, blank=True, related_name='actividades')
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True, related_name='actividades_principal')
    salas_secundarias = models.ManyToManyField(Sala, related_name='actividades_secundarias', blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    actividades = models.ManyToManyField(Actividad, related_name='usuarios_inscritos', blank=True)

    def __str__(self):
        return self.nombre