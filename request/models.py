from django.db import models
from project.models import Project

# Create your models here.
class Request(models.Model):
    type = models.CharField(max_length=32)
    spec_url = models.CharField(max_length=64)
    project=models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    