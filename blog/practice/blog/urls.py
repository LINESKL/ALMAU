from django.urls import path
from .views import blog_list, blog_create, blog_delete

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('<int:pk>/delete/', blog_delete, name='blog_delete'),
]