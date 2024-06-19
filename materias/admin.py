from django.contrib import admin
from .models import Carrera, Entrega, Facultad, Materia, TipoArchivo, Tarea
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Entrega)
admin.site.register(Facultad)
admin.site.register(TipoArchivo)
admin.site.register(Materia)
admin.site.register(Tarea)