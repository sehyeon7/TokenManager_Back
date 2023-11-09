from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TokenTime
from project.models import Project
from .serializers import TokenTimeSerializer

# Create your views here.
class TokenTimeListView(APIView):
  def get(self, request): #프로젝트에 등록되어 있는 모든 토큰시간 가져오기
    project_id = request.GET.get('project') #request.GET.get('project')의 의미 : project라는 이름의 파라미터를 가져온다.
    if not project_id:
      return Response({"detail": "프로젝트 id가 누락되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
    if not Project.objects.filter(id=project_id).exists():
      return Response({"detail": "프로젝트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    token_time_list = TokenTime.objects.filter(project=project_id)
    serializer = TokenTimeSerializer(token_time_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request): #토큰시간 추가
    if not request.user.is_authenticated:
      return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
    
    project_id = request.data.get('project')
    token_name = request.data.get('tokenname')
    time_limit = request.data.get('timelimit')

    if not project_id or not token_name or not time_limit:
      return Response({"detail": "누락된 필드값, ['project', 'tokenname', 'timelimit']"}, status=status.HTTP_400_BAD_REQUEST)
    if not Project.objects.filter(id=project_id).exists():
      return Response({"detail": "프로젝트를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    if TokenTime.objects.filter(project=project_id, tokenname=token_name).exists():
      return Response({"detail": "이미 존재하는 토큰입니다."}, status=status.HTTP_409_CONFLICT)
    
    token_time = TokenTime.objects.create(project_id=project_id, tokenname=token_name, timelimit=time_limit)
    serializer = TokenTimeSerializer(token_time)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class TokenTimeDetailView(APIView):
  def delete(self):
    pass