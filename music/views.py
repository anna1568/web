from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from music.models import Office, Specialization, Student, Teacher, Visiting

# Create your views here.
class ShowStudentsView(TemplateView):
    template_name = "music/show_students.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Student.objects.all()

        return context
    
class ShowTeacherView(TemplateView):
    template_name = "music/show_students.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Teacher.objects.all()

        return context

class ShowSpecializationsView(TemplateView):
    template_name = "music/show_specializations.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Specialization.objects.all()

        return context

class ShowOfficesView(TemplateView):
    template_name = "music/show_offices.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Office.objects.all()

        return context
    
class ShowVisitingsView(TemplateView):
    template_name = "music/show_visitings.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Visiting.objects.all()

        return context
