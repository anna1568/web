from rest_framework import serializers
from .models import Specialization, Student, Teacher, Office, Visiting

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = "__all__"

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"

class VisitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiting
        fields = "__all__"