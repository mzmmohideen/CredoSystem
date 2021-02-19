from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100, primary_key=True)
    course_duration  = models.IntegerField()
