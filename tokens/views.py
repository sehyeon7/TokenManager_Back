from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .serializers import TokensSerializer
from .models import Tokens
from Request.models import Request

class TokensListView(APIView):
    def get(self, request):
        tokens=Tokens.objects.all()
        serializer=TokensSerializer(tokens, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        token_name=request.data.get('token_name')
        content=request.data.get('content')
        request_id=request.data.get('request')
        tokenTime=request.data.get('tokenTime')
        
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)

        if not token_name or not content or not request_id or not tokenTime:
            return Response({"detail": "missing fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not Request.objects.filter(id=request_id).exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        token = Tokens.objects.create(token_name=token_name, content=content, request_id=request_id, tokenTime=tokenTime)
        serializer=TokensSerializer(token, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class TokensDetailView(APIView):
    def delete(self, request, token_id):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token=Tokens.objects.get(id=token_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



