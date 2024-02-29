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
        request_id = request.GET.get('request')
        if not Request.objects.filter(id=request_id).exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token_list = Tokens.objects.filter(request=request_id)
        serializer=TokensSerializer(token_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        token_name=request.data.get('token_name')
        content=request.data.get('content')
        request_id=request.data.get('request')
        expires_at=request.data.get('expiredAt')
        
        if not token_name or not content or not request_id or not expires_at:

            return Response({"detail": "missing fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not Request.objects.filter(id=request_id).exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not TokenTime.objects.filter(tokenname=token_name).exists():
            return Response({"detail": "Create the token time for the token first."}, status=status.HTTP_404_NOT_FOUND)
        
        for tokentime in TokenTime.objects.all():
            if (tokentime.tokenname==token_name):
                tokenTime=tokentime
        
        token = Tokens.objects.create(token_name=token_name, content=content, request_id=request_id, tokenTime=tokenTime, expires_at=expires_at)
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

class TokenExpiredView(APIView):
    def post(self, request):
        expired_tokens=request.data.get('expired_tokens')
        expired_token_id = [int(num) for num in expired_tokens.split('*') if num]

        full_token_list=Tokens.objects.filter(id__in=expired_token_id).update(is_expired=1)

        serializer = TokensSerializer(full_token_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


