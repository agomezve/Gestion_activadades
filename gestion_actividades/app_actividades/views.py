from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UsuarioInscrito, Monitor, ResponsableSala, Sala, Actividad


def lista_actividades(request):
    tipo = request.GET.get('tipo')
    monitor_id = request.GET.get('monitor')
    
    actividades = Actividad.objects.all()
    if tipo:
        actividades = actividades.filter(tipo__icontains=tipo)
    if monitor_id:
        actividades = actividades.filter(monitor_id=monitor_id)
        
    data = list(actividades.values("id", "nombre", "tipo", "horario", "descripcion", "duracion", "plazas_disponibles", "monitor_id", "sala_principal_id"))
    return JsonResponse(data, safe=False)

@csrf_exempt
def nueva_actividad(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            actividad = Actividad.objects.create(
                nombre=data['nombre'],
                tipo=data['tipo'],
                horario=data['horario'],
                descripcion=data['descripcion'],
                duracion=data['duracion'],
                plazas_disponibles=data['plazas_disponibles'],
                monitor_id=data['monitor_id'],
                sala_principal_id=data.get('sala_principal_id')
            )
            return JsonResponse({"mensaje": "Actividad creada con éxito", "id": actividad.id})
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo requerido: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_actividad(request, id):
    try:
        actividad = Actividad.objects.get(id=id)
        data = {
            "id": actividad.id,
            "nombre": actividad.nombre,
            "tipo": actividad.tipo,
            "horario": actividad.horario,
            "descripcion": actividad.descripcion,
            "duracion": str(actividad.duracion),
            "plazas_disponibles": actividad.plazas_disponibles,
            "monitor_id": actividad.monitor_id,
            "sala_principal_id": actividad.sala_principal_id,
        }
        return JsonResponse(data)
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

@csrf_exempt
def editar_actividad(request, id):
    if request.method in ['POST', 'PUT']:
        try:
            data = json.loads(request.body)
            actividad = Actividad.objects.get(id=id)
            if 'nombre' in data: actividad.nombre = data['nombre']
            if 'tipo' in data: actividad.tipo = data['tipo']
            if 'horario' in data: actividad.horario = data['horario']
            if 'descripcion' in data: actividad.descripcion = data['descripcion']
            if 'duracion' in data: actividad.duracion = data['duracion']
            if 'plazas_disponibles' in data: actividad.plazas_disponibles = data['plazas_disponibles']
            if 'monitor_id' in data: actividad.monitor_id = data['monitor_id']
            if 'sala_principal_id' in data: actividad.sala_principal_id = data['sala_principal_id']
            actividad.save()
            return JsonResponse({"mensaje": "Actividad actualizada con éxito"})
        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_actividad(request, id):
    if request.method in ['POST', 'DELETE']:
        try:
            actividad = Actividad.objects.get(id=id)
            actividad.delete()
            return JsonResponse({"mensaje": "Actividad eliminada con éxito"})
        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)


def lista_usuarios(request):
    actividad_id = request.GET.get('actividad')
    usuarios = UsuarioInscrito.objects.all()
    if actividad_id:
        usuarios = usuarios.filter(actividades__id=actividad_id)
        
    data = list(usuarios.values("id", "nombre", "edad", "email", "telefono"))
    return JsonResponse(data, safe=False)

@csrf_exempt
def nuevo_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = UsuarioInscrito.objects.create(
                nombre=data['nombre'],
                edad=data['edad'],
                email=data['email'],
                telefono=data['telefono']
            )
            return JsonResponse({"mensaje": "Usuario creado con éxito", "id": usuario.id})
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo requerido: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_usuario(request, id):
    try:
        usuario = UsuarioInscrito.objects.values("id", "nombre", "edad", "email", "telefono").get(id=id)
        return JsonResponse(usuario)
    except UsuarioInscrito.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

@csrf_exempt
def editar_usuario(request, id):
    if request.method in ['POST', 'PUT']:
        try:
            data = json.loads(request.body)
            usuario = UsuarioInscrito.objects.get(id=id)
            if 'nombre' in data: usuario.nombre = data['nombre']
            if 'edad' in data: usuario.edad = data['edad']
            if 'email' in data: usuario.email = data['email']
            if 'telefono' in data: usuario.telefono = data['telefono']
            usuario.save()
            return JsonResponse({"mensaje": "Usuario actualizado"})
        except UsuarioInscrito.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_usuario(request, id):
    if request.method in ['POST', 'DELETE']:
        try:
            usuario = UsuarioInscrito.objects.get(id=id)
            usuario.delete()
            return JsonResponse({"mensaje": "Usuario eliminado"})
        except UsuarioInscrito.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)


def lista_monitores(request):
    data = list(Monitor.objects.values("id", "nombre", "especializacion"))
    return JsonResponse(data, safe=False)

@csrf_exempt
def nuevo_monitor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            monitor = Monitor.objects.create(
                nombre=data['nombre'],
                especializacion=data['especializacion']
            )
            return JsonResponse({"mensaje": "Monitor creado con éxito", "id": monitor.id})
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo requerido: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_monitor(request, id):
    try:
        monitor = Monitor.objects.get(id=id)
        return JsonResponse({
            "id": monitor.id, 
            "nombre": monitor.nombre, 
            "especializacion": monitor.especializacion, 
            "numero_actividades_asignadas": monitor.numero_actividades_asignadas
        })
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)

@csrf_exempt
def editar_monitor(request, id):
    if request.method in ['POST', 'PUT']:
        try:
            data = json.loads(request.body)
            monitor = Monitor.objects.get(id=id)
            if 'nombre' in data: monitor.nombre = data['nombre']
            if 'especializacion' in data: monitor.especializacion = data['especializacion']
            monitor.save()
            return JsonResponse({"mensaje": "Monitor actualizado"})
        except Monitor.DoesNotExist:
            return JsonResponse({"error": "Monitor no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_monitor(request, id):
    if request.method in ['POST', 'DELETE']:
        try:
            monitor = Monitor.objects.get(id=id)
            monitor.delete()
            return JsonResponse({"mensaje": "Monitor eliminado"})
        except Monitor.DoesNotExist:
            return JsonResponse({"error": "Monitor no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def lista_salas(request):
    data = list(Sala.objects.values("id", "nombre", "capacidad", "ubicacion", "responsable_id"))
    return JsonResponse(data, safe=False)

@csrf_exempt
def nueva_sala(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sala = Sala.objects.create(
                nombre=data['nombre'],
                capacidad=data['capacidad'],
                ubicacion=data['ubicacion'],
                responsable_id=data['responsable_id']
            )
            return JsonResponse({"mensaje": "Sala creada con éxito", "id": sala.id})
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo requerido: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_sala(request, id):
    try:
        sala = Sala.objects.values("id", "nombre", "capacidad", "ubicacion", "responsable_id").get(id=id)
        return JsonResponse(sala)
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)

@csrf_exempt
def editar_sala(request, id):
    if request.method in ['POST', 'PUT']:
        try:
            data = json.loads(request.body)
            sala = Sala.objects.get(id=id)
            if 'nombre' in data: sala.nombre = data['nombre']
            if 'capacidad' in data: sala.capacidad = data['capacidad']
            if 'ubicacion' in data: sala.ubicacion = data['ubicacion']
            if 'responsable_id' in data: sala.responsable_id = data['responsable_id']
            sala.save()
            return JsonResponse({"mensaje": "Sala actualizada"})
        except Sala.DoesNotExist:
            return JsonResponse({"error": "Sala no encontrada"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar_sala(request, id):
    if request.method in ['POST', 'DELETE']:
        try:
            sala = Sala.objects.get(id=id)
            sala.delete()
            return JsonResponse({"mensaje": "Sala eliminada"})
        except Sala.DoesNotExist:
            return JsonResponse({"error": "Sala no encontrada"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

def listar_inscripciones_actividad(request, id):
    try:
        actividad = Actividad.objects.get(id=id)
        usuarios = actividad.usuarios.values("id", "nombre", "email")
        return JsonResponse(list(usuarios), safe=False)
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

@csrf_exempt
def inscribir_usuario(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            actividad = Actividad.objects.get(id=id)
            usuario = UsuarioInscrito.objects.get(id=data['usuario_id'])
            actividad.usuarios.add(usuario)
            return JsonResponse({"mensaje": "Usuario inscrito en la actividad"})
        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)
        except UsuarioInscrito.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Se requiere usuario_id en el JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def cancelar_inscripcion(request, id, usuario_id):
    if request.method in ['POST', 'DELETE']:
        try:
            actividad = Actividad.objects.get(id=id)
            usuario = UsuarioInscrito.objects.get(id=usuario_id)
            actividad.usuarios.remove(usuario)
            return JsonResponse({"mensaje": "Inscripción cancelada"})
        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)
        except UsuarioInscrito.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)
