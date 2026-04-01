from django.db import models
from cpf_field.models import CPFField
from course.models import Curse

TITULACOES = [ ("GR", "Graduado"),
    ("ME", "Mestre"),
    ("DR", "Doutor"),
    ]

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    cpf = CPFField('cpf')
    email = models.EmailField(unique=True)
    academic_degree = models.CharField(max_length=2, choices=TITULACOES)
    curse = models.ForeignKey(Curse, on_delete=models.PROTECT, related_name='teachercurse')
    

    def __str__(self):
        return self.name

    