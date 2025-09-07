from django.contrib import admin

from music.models import Office, Specialization, Student, Teacher, Visiting

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization']

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization']

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']

@admin.register(Visiting)
class VisitingAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'status', 'student', 'teacher', 'office']