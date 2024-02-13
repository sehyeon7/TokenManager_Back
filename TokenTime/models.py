from django.db import models
from project.models import Project

# Create your models here.
class TokenTime(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  tokenname = models.CharField(max_length=64)
  timelimit = models.CharField(max_length=256)