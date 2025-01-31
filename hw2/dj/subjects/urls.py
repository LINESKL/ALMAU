from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView, course_list

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses_list/', course_list, name='course-list'),
]