from django.db import models

class UsuarioInscrito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    especializacion = models.CharField(max_length=100)

    @property
    def numero_actividades_asignadas(self):
        return self.actividad_set.count()

    def __str__(self):
        return self.nombre

class ResponsableSala(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)
    responsable = models.OneToOneField(ResponsableSala, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.DurationField()
    plazas_disponibles = models.PositiveIntegerField()
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    sala_principal = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, related_name='actividades_principales')
    salas_secundarias = models.ManyToManyField(Sala, related_name='actividades_secundarias', blank=True)
    usuarios = models.ManyToManyField(UsuarioInscrito, related_name='actividades')

    def __str__(self):
        return self.nombre