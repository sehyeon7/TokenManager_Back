from django.urls import path
from .views import TokenTimeListView, TokenTimeDetailView

app_name = 'TokenTime'
urlpatterns = [
    path("", TokenTimeListView.as_view()),
    path("<int:token_time_id>/", TokenTimeDetailView.as_view()),
]