from django.contrib import admin

from music.models import Specialization, Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization']

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']