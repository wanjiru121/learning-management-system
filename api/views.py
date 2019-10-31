from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from course.models import Course,LessonPlan,Assignment
from department.models import Department
from .serializers import StudentSerializer,TrainerSerializer,CourseSerializer,DepartmentSerializer,LessonPlanSerializer,AssignmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TrainerViewSet(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class LessonPlanViewSet(viewsets.ModelViewSet):
    serializer_class = LessonPlanSerializer
    queryset = LessonPlan.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


