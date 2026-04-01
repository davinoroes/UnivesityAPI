from django.contrib import admin
from course.models import Curse

@admin.register(Curse)
class CurseAdmin(admin.ModelAdmin):
    list_display = ('name','curse_code','semesters')
