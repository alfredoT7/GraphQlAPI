import graphene 
from graphene_django import DjangoObjectType
from usuarios.models import UserN, Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = "__all__"#los campos que quiera

class Query(graphene.ObjectType):
    hello=graphene.String(default_value="Hello!")
    students = graphene.List(StudentType)

    def resolve_userN(self, info):
        return UserN.objects.all()
    
    def resolve_students(self, info):
        return Student.objects.all()
    
schema=graphene.Schema(query=Query)