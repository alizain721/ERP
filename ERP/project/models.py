from django.db import models

# Create your models here.
class Project(models.Model):
    """Project model class"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
