from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from teachers.models import Teacher

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    discipline_code = models.CharField(max_length=9)
    credit_hours = models.IntegerField(validators=[
        MinValueValidator(32, "A duração mínima de uma disciplina é 32 horas"),
        MaxValueValidator(96, "A duração máxima de uma disciplina é 96 horas"),
    ])
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,related_name='disciplineteacher')

    def __str__(self):
        return self.name
