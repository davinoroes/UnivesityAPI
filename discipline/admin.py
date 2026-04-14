from django.contrib import admin
from discipline.models import Discipline

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name','discipline_code','teacher')