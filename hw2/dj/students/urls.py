from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView, student_list

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('students_list/', student_list, name='student-list'),

]