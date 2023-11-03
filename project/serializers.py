from rest_framework.serializers import ModelSerializer
from .models import Project
from account.serializers import UserSerializer

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"