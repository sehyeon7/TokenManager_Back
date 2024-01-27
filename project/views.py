from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectListView(APIView):
    def get(self, request): #로그인한 유저가 생성한 프로젝트 리스트
        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        projects = Project.objects.filter(author=user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request): #프로젝트 생성
        author = request.user
        url = request.data.get('url')

        if not author.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not url:
            return Response({"detail": "url을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
        project = Project.objects.create(author=author, url=url)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetailView(APIView):
    def get(self, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response({"detail": "프로젝트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, project_id): #프로젝트 수정
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response({"detail": "프로젝트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        if not request.data['url'] or request.data['url'] == "":
            return Response({"detail": "url을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        project.url = request.data.get('url')
        project.save()
        return Response({"detail": "프로젝트명이 성공적으로 수정되었습니다"}, status=status.HTTP_200_OK)
    
    def delete(self, request, project_id): #프로젝트 삭제
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response({"detail": "프로젝트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        project.delete()
        return Response({"detail": "프로젝트가 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)