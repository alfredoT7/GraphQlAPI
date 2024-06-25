import graphene 
from graphene_django import DjangoObjectType
from usuarios.models import UserN, Student, Teacher
from materias.models import Facultad, Carrera, Materia, Tarea, TipoArchivo, Entrega

#estudiantes
class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ["id", "email", "first_name", "last_name", "birth_date", "matricula_active"]
#Docentes
class TeacherType(DjangoObjectType):
    class Meta:
        model= Teacher
        fields = ["id", "email", "first_name", "last_name", "birth_date", "teacher_since"]

class FacultadType(DjangoObjectType):
    class Meta:
        model = Facultad
        fields = "__all__"

class CarreraType(DjangoObjectType):
    class Meta:
        model = Carrera
        fields = "__all__"

class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia
        fields = "__all__"

class TareaType(DjangoObjectType):
    class Meta:
        model = Tarea
        fields = "__all__"

class TipoArchivoType(DjangoObjectType):
    class Meta:
        model = TipoArchivo
        fields = "__all__"

class EntregaType(DjangoObjectType):
    class Meta:
        model = Entrega
        fields = "__all__"

class Query(graphene.ObjectType):
    students = graphene.List(StudentType)
    student_by_ID = graphene.List(StudentType, id=graphene.ID())
    teachers = graphene.List(TeacherType)
    teacher_by_ID = graphene.List(TeacherType, id=graphene.ID())
    facultades = graphene.List(FacultadType)
    carreras = graphene.List(CarreraType)
    materias = graphene.List(MateriaType)
    materias_by_ID= graphene.List(MateriaType, id=graphene.ID())
    tareas = graphene.List(TareaType)
    tipo_archivos = graphene.List(TipoArchivoType)
    #entregas = graphene.List(EntregaType)
    
    # materias_por_carrera = graphene.List(MateriaType, carrera_id=graphene.Int(required=True))
    # tareas_por_materia = graphene.List(TareaType, materia_id=graphene.Int(required=True))
    # entregas_por_tarea = graphene.List(EntregaType, tarea_id=graphene.Int(required=True))
    # estudiantes_por_materia = graphene.List(StudentType, materia_id=graphene.Int(required=True))


    def resolve_students(self, info):
        return Student.objects.all()
    
    def resolve_student_by_ID(self, info, id):
        return Student.objects.filter(pk=id)

    def resolve_teachers(self, info):
        return Teacher.objects.all()
    
    def resolve_teacher_by_ID(self, info, id):
        return Teacher.objects.filter(pk=id)

    def resolve_facultades(self, info):
        return Facultad.objects.all()
    
    def resolve_carreras(self, info):
        return Carrera.objects.all()
    
    def resolve_materias(self, info):
        return Materia.objects.all()
    
    def resolve_materias_by_ID(self, info, id):
        return Materia.objects.filter(pk=id)

    def resolve_tareas(self, info):
        return Tarea.objects.all()
    
    def resolve_tipo_archivos(self, info):
        return TipoArchivo.objects.all()
    
    def resolve_entregas(self, info):
        return Entrega.objects.all()
    
    #complejasd
    # def resolve_materias_por_carrera(self, info, carrera_id):
    #     return Materia.objects.filter(carreras__id=carrera_id)

    # def resolve_tareas_por_materia(self, info, materia_id):
    #     return Tarea.objects.filter(materia__id=materia_id)

    # def resolve_entregas_por_tarea(self, info, tarea_id):
    #     return Entrega.objects.filter(tarea__id=tarea_id)
    
    # def resolve_estudiantes_por_materia(self, info, materia_id):
    #     return Student.objects.filter(inscripcion__id=materia_id)

schema=graphene.Schema(query=Query)