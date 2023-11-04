from django.urls import path
from .views import TokenTimeListView, TokenTimeDetailView

app_name = 'tokentime'
urlpatterns = [
    path("", TokenTimeListView.as_view()),
    path("<int:project_id>/", TokenTimeDetailView.as_view()),
]