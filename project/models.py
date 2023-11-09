from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Project(models.Model):
  author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
  url = models.CharField(max_length=512)