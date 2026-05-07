# Gestión de Actividades - Centro Cultural

## Contexto del Proyecto
Aplicación web desarrollada con **Django** para un centro cultural municipal. Su objetivo es digitalizar la gestión de actividades y talleres para mejorar la experiencia de los usuarios y facilitar el trabajo del personal, reemplazando el antiguo sistema basado en papel para evitar errores, duplicidades y pérdida de información.

## Características Principales
- **Gestión de Actividades:** Creación, edición, visualización y eliminación de actividades (con control de plazas, horarios y duración).
- **Gestión de Usuarios Inscritos:** Alta y administración de usuarios, así como la gestión de sus inscripciones a múltiples actividades.
- **Gestión de Monitores:** Registro de monitores especializados y su asignación como responsables de impartir las actividades.
- **Gestión de Salas:** Administración de los espacios del centro. Cada actividad puede tener una sala principal y salas secundarias compartidas (siempre que no haya solapamiento de horarios).
- **Responsables de Sala:** Asignación de un responsable técnico único por cada sala.

## Tecnologías y Arquitectura
- **Backend:** Python con Django framework.
- **Frontend:** Templates nativos de Django (HTML/CSS).
- **Arquitectura:** Diseño basado en el patrón **MVT** (Model-View-Template) propio de Django, respaldado por diagramas de arquitectura basados en el **Modelo C4**.

## Modelos del Dominio (Entidades)
1. **Actividad:** Nombre, tipo, horario, descripción, duración, plazas disponibles.
2. **Usuario:** Nombre, edad, email, teléfono.
3. **Monitor:** Nombre, especialización, número de actividades asignadas.
4. **Sala:** Nombre, capacidad, ubicación.
5. **ResponsableSala:** Encargado técnico (relación 1 a 1 con la Sala).

## Endpoints Principales
El sistema incluye rutas CRUD completas para todas las entidades, como por ejemplo:
- `/actividades/` , `/usuarios/`, `/monitores/`, `/salas/`
- Rutas de gestión de inscripciones: `/actividades/<id>/inscribir/`
- Filtros de búsqueda (ej. por tipo de actividad o por monitor).

## Instalación y Ejecución Local
1. Clona este repositorio.
2. Crea un entorno virtual e instala las dependencias de Django.
3. Ejecuta las migraciones de la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
5. Accede a la aplicación desde `http://127.0.0.1:8000/`.
