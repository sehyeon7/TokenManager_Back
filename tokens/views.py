from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .serializers import TokensSerializer
from .models import Tokens
from request.models import Request
from TokenTime.models import TokenTime

class TokensListView(APIView):
    def get(self, request):
        tokens=Tokens.objects.all()
        serializer=TokensSerializer(tokens, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        token_name=request.data.get('token_name')
        content=request.data.get('content')
        request_id=request.data.get('request')
        
        if not token_name or not content or not request_id:
            return Response({"detail": "missing fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not Request.objects.filter(id=request_id).exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not TokenTime.objects.filter(tokenname=token_name).exists():
            return Response({"detail": "Create the token time for the token first."}, status=status.HTTP_404_NOT_FOUND)
        
        for tokentime in TokenTime.objects.all():
            if (tokentime.tokenname==token_name):
                tokenTime=tokentime
        
        token = Tokens.objects.create(token_name=token_name, content=content, request_id=request_id, tokenTime=tokenTime)
        serializer=TokensSerializer(token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class TokensDetailView(APIView):
    def delete(self, request, token_id):
        try:
            token=Tokens.objects.get(id=token_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



