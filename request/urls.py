from django.urls import path

from .views import RequestListView, RequestDetailView

app_name = 'request'
urlpatterns= [
    path("", RequestListView.as_view()),
    path("<int:request_id>/", RequestDetailView.as_view())
]