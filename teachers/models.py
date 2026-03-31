from django.db import models
from cpf_field.models import CPFField

TITULACOES = [ ("GR", "Graduado"),
    ("ME", "Mestre"),
    ("DR", "Doutor"),
    ]

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    cpf = CPFField('cpf')
    email = models.EmailField(unique=True)
    academic_degree = models.CharField(max_length=2, choices=TITULACOES)
    

    def __str__(self):
        self.name

    