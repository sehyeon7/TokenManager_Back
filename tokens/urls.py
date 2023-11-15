from django.urls import path

from .views import TokensListView, TokensDetailView

app_name = 'tokens'
urlpatterns= [
    path("", TokensListView.as_view()),
    path("<int:token_id>/", TokensDetailView.as_view())
]