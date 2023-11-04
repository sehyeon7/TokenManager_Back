from django.db import models

# Create your models here.
class Request(models.Model):
    type = models.CharField(max_length=32)
    spec_url = models.CharField(max_length=64)