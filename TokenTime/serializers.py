from rest_framework.serializers import ModelSerializer
from .models import TokenTime
from account.serializers import UserSerializer

class TokenTimeSerializer(ModelSerializer):
    class Meta:
        model = TokenTime
        fields = "__all__"