from django.db import models
from usuarios.models import Teacher,Student
from django.core.validators import MinValueValidator, MaxValueValidator


class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    name_facultad = models.CharField(max_length=60)

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    name_carrera = models.CharField(max_length=100, null=False)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"La {self.name_carrera} es parte de la facultad con id: {self.facultad}"

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    docente = models.ManyToManyField(Teacher, related_name='docente_materia')
    name_materia = models.CharField(max_length=60, null=False)
    carreras = models.ManyToManyField(Carrera, related_name='materia_carrera')
    estudiante= models.ManyToManyField(Student, related_name='inscripcion')

    def __str__(self):
        return self.name_materia

class Tarea(models.Model):
    id_tarea= models.AutoField(primary_key=True)
    nombre_tarea=models.CharField(max_length=20, null=False)
    fecha_asignacion=models.DateField(null=False)
    fecha_entrega=models.DateField(null=True)
    descripcion=models.CharField(null=False, max_length=200)
    materia=models.ManyToManyField(Materia, related_name='tarea_materia')

class TipoArchivo(models.Model):
    id_tipo_archivo=models.AutoField(primary_key=True)
    tipo_archivo=models.CharField(max_length=100, null=False)

class Entrega(models.Model):
    id_entrega=models.AutoField(primary_key=True)
    tipo_archivo=models.ForeignKey(TipoArchivo,null=True,on_delete=models.CASCADE)
    retraso_entrega=models.DateField(null=False)
    calificacion=models.IntegerField(null=False, validators=[MinValueValidator(1),MaxValueValidator(100)])
    tarea=models.ManyToManyField(Tarea, related_name='tarea_entrega')
    archivo=models.BinaryField(null=True, )
    def __str__(self):
        return self.calificacion


    
