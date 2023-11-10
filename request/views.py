from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import RequestSerializer
from .models import Request

# Create your views here.
class RequestListView(APIView):
    def get(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        type = request.data.get('type')
        spec_url = request.data.get('spec_url')

        if not type or not spec_url:
            return Response({"detail": "fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        request = Request.objects.create(type=type, spec_url=spec_url)

        serializer = RequestSerializer(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RequestDetailView(APIView):
    def delete(self, request, request_id):
        try:
            request = Request.objects.get(id=request_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
