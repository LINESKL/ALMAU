from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import render

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'subjects/course_list.html', {'courses': courses})