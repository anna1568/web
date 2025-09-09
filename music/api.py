from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from music.models import Student, Teacher, Specialization, Office, Visiting
from music.serializers import StudentSerializer, TeacherSerializer, SpecializationSerializer, OfficeSerializer, VisitingSerializer

class StudentViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SpecializationViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class OfficeViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class VisitingViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Visiting.objects.all()
    serializer_class = VisitingSerializer
