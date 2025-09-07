from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = name = models.TextField("Специальность")

class Student(models.Model):
    name = models.TextField("ФИО")
    specialization = models.ForeignKey("Specialization", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return self.name