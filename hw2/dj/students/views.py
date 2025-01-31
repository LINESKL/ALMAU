from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})