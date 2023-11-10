from rest_framework.serializers import ModelSerializer
from .models import Tokens

class TokensSerializer(ModelSerializer):
    class Meta:
        model = Tokens
        fields = "__all__"