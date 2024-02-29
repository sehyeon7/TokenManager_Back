from django.urls import path

from .views import TokensListView, TokensDetailView, TokenExpiredView

app_name = 'tokens'
urlpatterns= [
    path("", TokensListView.as_view()),
    path("<int:token_id>/", TokensDetailView.as_view()),
    path("expired/", TokenExpiredView.as_view())
]