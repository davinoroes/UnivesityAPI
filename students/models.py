from django.db import models
from cpf_field.models import CPFField
from course.models import Curse
from enrollments.models import Enrollment
from discipline.models import Discipline



class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = CPFField('cpf') #com isso já valido o cpf
    curse = models.ForeignKey(Curse, on_delete=models.PROTECT, related_name='studentcurse') #vou colocar uma foreign key com o model do curso (vou fazer uma app para curso)
    
    grade = models.ManyToManyField(Discipline, through=Enrollment,related_name='studentsgrade') #manytomany com o model Materias, e vou usar o throug com o model Matrícula

    def __str__(self):
        return self.name

