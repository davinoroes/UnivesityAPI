from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

COURSE_CHOICES = [
    ('CS', 'Ciência da Computação'),
    ('ENGC', 'Engenharia Civil'),
    ('MED', 'Medicina'),
    ('DIR', 'Direito'),
    ('ADM', 'Administração'),
    ('ECO', 'Economia'),
    ('PSQ', 'Psicologia'),
    ('ENF', 'Enfermagem'),
    ('ARQ', 'Arquitetura'),
    ('PED', 'Pedagogia'),
]


class Curse(models.Model):
    name = models.CharField(choices=COURSE_CHOICES)
    curse_code = models.CharField(max_length=6) 
    semesters = models.IntegerField(validators=[
        MinValueValidator(8, "A duração mínima dos cursos são 8 semestres "),
        MaxValueValidator(12, "A duração máxima dos cursos são 12 semestres"),
    ])

    def __str__(self):
        return self.name
