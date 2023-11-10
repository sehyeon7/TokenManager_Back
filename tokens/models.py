from django.db import models
from TokenTime.models import TokenTime
from request.models import Request

# Create your models here.
class Tokens(models.Model):
    token_name=models.CharField(max_length=64)
    content=models.CharField(max_length=64)
    tokenTime=models.ForeignKey(TokenTime, null=True, on_delete=models.CASCADE)
    request=models.ForeignKey(Request, null=True, on_delete=models.CASCADE)