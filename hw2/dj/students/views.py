from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.views.decorators.csrf import csrf_protect

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'students/student_list.html', {'students': students, 'form': form})

# @csrf_protect
# def get_students_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         form = StudentForm()
#         return render(request, 'students/student_list.html', {'students': students, 'form': form})
#
#     elif request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('api/students_list')
#         else:
#             students = Student.objects.all()
#             return render(request, 'students/student_list.html', {'students': students, 'form': form})