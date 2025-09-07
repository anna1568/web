from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from music.models import Student

# Create your views here.
class ShowStudentsView(TemplateView):
    template_name = "music/show_students.html"

    def get_context_data(self, **kwargs : Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['music'] = Student.objects.all()

        return context

