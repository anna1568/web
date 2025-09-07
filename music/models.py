from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = models.TextField("Специальность")
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name = models.TextField("ФИО")
    specialization = models.ForeignKey("Specialization", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return self.name
    
class Teacher(models.Model):
    name = models.TextField("ФИО")
    specialization = models.ForeignKey("Specialization", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    
    def __str__(self) -> str:
        return self.name
    
class Office(models.Model):
    number = models.CharField("Номер кабинета")
    
    class Meta:
        verbose_name = "Номер кабинета"
        verbose_name_plural = "Номера кабинетов"
   
    def __str__(self) -> str:
        return self.number

class Visiting(models.Model):
    date = models.DateField("Дата посещения")
    time = models.TimeField("Время посещения")
    status = models.BooleanField("Статус посещения")
    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True)
    office = models.ForeignKey("Office", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещение"
    