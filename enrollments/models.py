from django.db import models
from students.models import Student
from discipline.models import Discipline

class Enrollment(models.Model):
    students = models.ForeignKey(Student,on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    semester = models.CharField(max_length=6) #tipo 2026.1
    final_note = models.IntegerField(null=True,blank=True)
    approved = models.BooleanField(default=False)

