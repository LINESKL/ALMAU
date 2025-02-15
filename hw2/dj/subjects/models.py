from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

