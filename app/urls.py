"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from music.api import StudentViewset, TeacherViewset, SpecializationViewset, OfficeViewset, VisitingViewset
from music import views

router = DefaultRouter()
router.register("students", StudentViewset, basename="students")
router.register("teachers", TeacherViewset, basename="teachers")
router.register("specializations", SpecializationViewset, basename="specializations")
router.register("offices", OfficeViewset, basename="offices")
router.register("visitings", VisitingViewset, basename="visitings")

urlpatterns = [
    path('', views.ShowStudentsView.as_view(), name='show_students'),
    path('teachers/', views.ShowTeacherView.as_view(), name='show_teachers'),
    path('specializations/', views.ShowSpecializationsView.as_view(), name='show_specializations'),
    path('offices/', views.ShowOfficesView.as_view(), name='show_offices'),
    path('visitings/', views.ShowVisitingsView.as_view(), name='show_visitings'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


